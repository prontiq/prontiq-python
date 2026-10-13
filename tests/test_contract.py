import json
from pathlib import Path

import httpx
import pytest

from prontiq import AuthenticatedClient
from prontiq.api.address import (
    autocomplete_address,
    enrich_address,
    lookup_postcode,
    lookup_suburb,
    reverse_geocode_address,
    validate_address,
)
from prontiq.errors import UnexpectedStatus
from prontiq.models.address_document import AddressDocument
from prontiq.models.enrich_address_response import EnrichAddressResponse

FIXTURES = json.loads((Path(__file__).parent / "fixtures/schema11.json").read_text())
SITE, LOCALITY, STREET = FIXTURES
SUGGESTION = {
    key: SITE["address"][key]
    for key in ("id", "addressLabel", "localityName", "state", "postcode")
} | {"prontiqMatchScore": 99, "prontiqMatchQuality": "high"}
CASES = [
    (
        autocomplete_address,
        "/v1/address/autocomplete",
        {"q": "abbotts", "state": "ot"},
        {"suggestions": [SUGGESTION], "total": 1},
    ),
    (
        validate_address,
        "/v1/address/validate",
        {"q": "2 abbotts nest"},
        {
            "match": STREET["address"],
            "prontiqMatchScore": 99,
            "prontiqMatchQuality": "high",
        },
    ),
    (
        enrich_address,
        "/v1/address/enrich",
        {"id": LOCALITY["address"]["id"]},
        LOCALITY["enrich"],
    ),
    (
        reverse_geocode_address,
        "/v1/address/reverse",
        {"lat": -10.43384769, "lon": 105.6707055},
        {"results": [SITE["address"] | {"distance_m": 0.0}], "total": 1},
    ),
    (
        lookup_postcode,
        "/v1/address/lookup/postcode",
        {"postcode": "6798"},
        {
            "postcode": "6798",
            "localities": [
                {"name": "CHRISTMAS ISLAND", "state": "OT", "address_count": 1}
            ],
        },
    ),
    (
        lookup_suburb,
        "/v1/address/lookup/suburb",
        {"suburb": "christmas island", "state": "ot"},
        {
            "suburb": "CHRISTMAS ISLAND",
            "state": "OT",
            "postcodes": ["6798"],
            "address_count": 1,
        },
    ),
]


def client_for(handler):
    return AuthenticatedClient(
        base_url="https://api.prontiq.dev",
        token="test-key",
        prefix="",
        auth_header_name="X-Api-Key",
        raise_on_unexpected_status=True,
        httpx_args={"transport": httpx.MockTransport(handler)},
    )


def response_handler(path, params, payload):
    def handle(request):
        assert request.method == "GET"
        assert request.url.path == path
        assert request.headers["X-Api-Key"] == "test-key"
        assert "authorization" not in request.headers
        for key, value in params.items():
            assert request.url.params[key] == str(value)
        assert request.url.params["debug"] == "false"
        return httpx.Response(200, json=payload)

    return handle


@pytest.mark.parametrize("operation,path,params,payload", CASES)
def test_sync_operations(operation, path, params, payload):
    with client_for(response_handler(path, params, payload)) as client:
        response = operation.sync_detailed(client=client, debug="false", **params)
    assert response.status_code == 200
    assert response.parsed.to_dict() == payload


@pytest.mark.parametrize("operation,path,params,payload", CASES)
async def test_async_operations(operation, path, params, payload):
    async with client_for(response_handler(path, params, payload)) as client:
        response = await operation.asyncio_detailed(
            client=client, debug="false", **params
        )
    assert response.status_code == 200
    assert response.parsed.to_dict() == payload


@pytest.mark.parametrize("record", FIXTURES)
def test_producer_records_preserve_fallbacks_and_source_release(record):
    address = AddressDocument.from_dict(record["address"])
    enriched = EnrichAddressResponse.from_dict(record["enrich"])
    assert address.to_dict() == record["address"]
    assert enriched.to_dict() == record["enrich"]
    assert enriched.source_data_release == "2026.08"
    assert address.state == "OT"
    if address.fallback_geocode is not None:
        assert address.location is None
        assert (
            address.fallback_geocode.latitude
            == record["address"]["fallbackGeocode"]["latitude"]
        )
        assert (
            address.fallback_geocode.longitude
            == record["address"]["fallbackGeocode"]["longitude"]
        )
    else:
        assert address.location is not None


def test_unknown_fallback_precision_and_nullable_fields():
    record = STREET["address"] | {"confidence": None, "boundaries": None}
    record["fallbackGeocode"] = record["fallbackGeocode"] | {"precision": "unknown"}
    assert AddressDocument.from_dict(record).to_dict() == record


@pytest.mark.parametrize("status", [400, 401, 403, 404, 429, 500])
def test_documented_errors_preserve_status_and_request_id(status):
    payload = {
        "error": {
            "code": {
                400: "INVALID_PARAMETERS",
                401: "INVALID_API_KEY",
                403: "PRODUCT_NOT_ALLOWED",
                404: "NOT_FOUND",
                429: "RATE_LIMITED",
                500: "INTERNAL_ERROR",
            }[status],
            "message": "Request failed",
            "status": status,
            "request_id": "req_test",
        }
    }
    with client_for(lambda _: httpx.Response(status, json=payload)) as client:
        response = enrich_address.sync_detailed(client=client, id="missing")
    assert response.status_code == status
    assert response.parsed.to_dict() == payload


def test_unexpected_status_raises():
    with client_for(lambda _: httpx.Response(502, text="Bad gateway")) as client:
        with pytest.raises(UnexpectedStatus):
            enrich_address.sync_detailed(client=client, id="missing")


def test_missing_required_fallback_is_rejected():
    record = dict(SITE["address"])
    del record["fallbackGeocode"]
    with pytest.raises(KeyError, match="fallbackGeocode"):
        AddressDocument.from_dict(record)

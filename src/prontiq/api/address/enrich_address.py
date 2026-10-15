from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.address_debug_query import AddressDebugQuery
from ...models.address_error_response import AddressErrorResponse
from ...models.enrich_address_response import EnrichAddressResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    id: str,
    debug: AddressDebugQuery | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["id"] = id

    json_debug: str | Unset = UNSET
    if not isinstance(debug, Unset):
        json_debug = debug

    params["debug"] = json_debug

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/address/enrich",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AddressErrorResponse | EnrichAddressResponse | None:
    if response.status_code == 200:
        response_200 = EnrichAddressResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = AddressErrorResponse.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = AddressErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = AddressErrorResponse.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = AddressErrorResponse.from_dict(response.json())

        return response_404

    if response.status_code == 429:
        response_429 = AddressErrorResponse.from_dict(response.json())

        return response_429

    if response.status_code == 500:
        response_500 = AddressErrorResponse.from_dict(response.json())

        return response_500

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[AddressErrorResponse | EnrichAddressResponse]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    id: str,
    debug: AddressDebugQuery | Unset = UNSET,
) -> Response[AddressErrorResponse | EnrichAddressResponse]:
    """Enrich an address by ID

     Return the richest public address document for a known G-NAF address `id` returned by Autocomplete,
    Validate, or Reverse geocode. Use this after a user selects an address when you need structured
    components, geocodes, boundaries, locality and street context, aliases, secondaries, and source-
    record metadata.

    Args:
        id (str): G-NAF address document ID. Paste an id value returned from Autocomplete or
            Validate. Example: GAQLD156786950.
        debug (AddressDebugQuery | Unset): Optional diagnostic flag. Send exactly `true` or
            `false`. Invalid values are rejected; debug diagnostics are for support only and must not
            be used for business decisions. Example: false.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddressErrorResponse | EnrichAddressResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        debug=debug,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    id: str,
    debug: AddressDebugQuery | Unset = UNSET,
) -> AddressErrorResponse | EnrichAddressResponse | None:
    """Enrich an address by ID

     Return the richest public address document for a known G-NAF address `id` returned by Autocomplete,
    Validate, or Reverse geocode. Use this after a user selects an address when you need structured
    components, geocodes, boundaries, locality and street context, aliases, secondaries, and source-
    record metadata.

    Args:
        id (str): G-NAF address document ID. Paste an id value returned from Autocomplete or
            Validate. Example: GAQLD156786950.
        debug (AddressDebugQuery | Unset): Optional diagnostic flag. Send exactly `true` or
            `false`. Invalid values are rejected; debug diagnostics are for support only and must not
            be used for business decisions. Example: false.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddressErrorResponse | EnrichAddressResponse
    """

    return sync_detailed(
        client=client,
        id=id,
        debug=debug,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    id: str,
    debug: AddressDebugQuery | Unset = UNSET,
) -> Response[AddressErrorResponse | EnrichAddressResponse]:
    """Enrich an address by ID

     Return the richest public address document for a known G-NAF address `id` returned by Autocomplete,
    Validate, or Reverse geocode. Use this after a user selects an address when you need structured
    components, geocodes, boundaries, locality and street context, aliases, secondaries, and source-
    record metadata.

    Args:
        id (str): G-NAF address document ID. Paste an id value returned from Autocomplete or
            Validate. Example: GAQLD156786950.
        debug (AddressDebugQuery | Unset): Optional diagnostic flag. Send exactly `true` or
            `false`. Invalid values are rejected; debug diagnostics are for support only and must not
            be used for business decisions. Example: false.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddressErrorResponse | EnrichAddressResponse]
    """

    kwargs = _get_kwargs(
        id=id,
        debug=debug,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    id: str,
    debug: AddressDebugQuery | Unset = UNSET,
) -> AddressErrorResponse | EnrichAddressResponse | None:
    """Enrich an address by ID

     Return the richest public address document for a known G-NAF address `id` returned by Autocomplete,
    Validate, or Reverse geocode. Use this after a user selects an address when you need structured
    components, geocodes, boundaries, locality and street context, aliases, secondaries, and source-
    record metadata.

    Args:
        id (str): G-NAF address document ID. Paste an id value returned from Autocomplete or
            Validate. Example: GAQLD156786950.
        debug (AddressDebugQuery | Unset): Optional diagnostic flag. Send exactly `true` or
            `false`. Invalid values are rejected; debug diagnostics are for support only and must not
            be used for business decisions. Example: false.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddressErrorResponse | EnrichAddressResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            id=id,
            debug=debug,
        )
    ).parsed

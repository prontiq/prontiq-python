"""Type-check the installed wheel, independently of the SDK source checks."""

from typing import assert_type

from prontiq import AuthenticatedClient
from prontiq.api.address import autocomplete_address
from prontiq.models import AddressErrorResponse, AutocompleteAddressResponse
from prontiq.types import Response


def check_sync(client: AuthenticatedClient) -> None:
    response = autocomplete_address.sync_detailed(client=client, q="Sydney")
    assert_type(response, Response[AddressErrorResponse | AutocompleteAddressResponse])
    assert_type(response.status_code, int)
    if isinstance(response.parsed, AutocompleteAddressResponse):
        assert_type(response.parsed.total, int)
    elif isinstance(response.parsed, AddressErrorResponse):
        assert_type(response.parsed.error.request_id, str)


async def check_async(client: AuthenticatedClient) -> None:
    response = await autocomplete_address.asyncio_detailed(client=client, q="Sydney")
    assert_type(response, Response[AddressErrorResponse | AutocompleteAddressResponse])

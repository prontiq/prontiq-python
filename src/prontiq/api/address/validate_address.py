from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.address_debug_query import AddressDebugQuery
from ...models.address_error_response import AddressErrorResponse
from ...models.validate_address_response import ValidateAddressResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    q: str,
    debug: AddressDebugQuery | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["q"] = q

    json_debug: str | Unset = UNSET
    if not isinstance(debug, Unset):
        json_debug = debug

    params["debug"] = json_debug

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/address/validate",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AddressErrorResponse | ValidateAddressResponse | None:
    if response.status_code == 200:
        response_200 = ValidateAddressResponse.from_dict(response.json())

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
) -> Response[AddressErrorResponse | ValidateAddressResponse]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    q: str,
    debug: AddressDebugQuery | Unset = UNSET,
) -> Response[AddressErrorResponse | ValidateAddressResponse]:
    """Validate an address

     Find the best G-NAF match for a submitted address string and classify request match quality. Use
    `prontiqMatchScore` and `prontiqMatchQuality` for acceptance thresholds and user prompts. If `match`
    is present, `match.confidence` is separate G-NAF source-record metadata for the address record.

    Args:
        q (str): Free-text address to validate against G-NAF. Include suburb, state, and postcode
            when available for the strongest match signal. Example: 9 endeavour court lammermoor qld
            4703.
        debug (AddressDebugQuery | Unset): Optional diagnostic flag. Send exactly `true` or
            `false`. Invalid values are rejected; debug diagnostics are for support only and must not
            be used for business decisions. Example: false.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddressErrorResponse | ValidateAddressResponse]
    """

    kwargs = _get_kwargs(
        q=q,
        debug=debug,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    q: str,
    debug: AddressDebugQuery | Unset = UNSET,
) -> AddressErrorResponse | ValidateAddressResponse | None:
    """Validate an address

     Find the best G-NAF match for a submitted address string and classify request match quality. Use
    `prontiqMatchScore` and `prontiqMatchQuality` for acceptance thresholds and user prompts. If `match`
    is present, `match.confidence` is separate G-NAF source-record metadata for the address record.

    Args:
        q (str): Free-text address to validate against G-NAF. Include suburb, state, and postcode
            when available for the strongest match signal. Example: 9 endeavour court lammermoor qld
            4703.
        debug (AddressDebugQuery | Unset): Optional diagnostic flag. Send exactly `true` or
            `false`. Invalid values are rejected; debug diagnostics are for support only and must not
            be used for business decisions. Example: false.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddressErrorResponse | ValidateAddressResponse
    """

    return sync_detailed(
        client=client,
        q=q,
        debug=debug,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    q: str,
    debug: AddressDebugQuery | Unset = UNSET,
) -> Response[AddressErrorResponse | ValidateAddressResponse]:
    """Validate an address

     Find the best G-NAF match for a submitted address string and classify request match quality. Use
    `prontiqMatchScore` and `prontiqMatchQuality` for acceptance thresholds and user prompts. If `match`
    is present, `match.confidence` is separate G-NAF source-record metadata for the address record.

    Args:
        q (str): Free-text address to validate against G-NAF. Include suburb, state, and postcode
            when available for the strongest match signal. Example: 9 endeavour court lammermoor qld
            4703.
        debug (AddressDebugQuery | Unset): Optional diagnostic flag. Send exactly `true` or
            `false`. Invalid values are rejected; debug diagnostics are for support only and must not
            be used for business decisions. Example: false.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddressErrorResponse | ValidateAddressResponse]
    """

    kwargs = _get_kwargs(
        q=q,
        debug=debug,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    q: str,
    debug: AddressDebugQuery | Unset = UNSET,
) -> AddressErrorResponse | ValidateAddressResponse | None:
    """Validate an address

     Find the best G-NAF match for a submitted address string and classify request match quality. Use
    `prontiqMatchScore` and `prontiqMatchQuality` for acceptance thresholds and user prompts. If `match`
    is present, `match.confidence` is separate G-NAF source-record metadata for the address record.

    Args:
        q (str): Free-text address to validate against G-NAF. Include suburb, state, and postcode
            when available for the strongest match signal. Example: 9 endeavour court lammermoor qld
            4703.
        debug (AddressDebugQuery | Unset): Optional diagnostic flag. Send exactly `true` or
            `false`. Invalid values are rejected; debug diagnostics are for support only and must not
            be used for business decisions. Example: false.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddressErrorResponse | ValidateAddressResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            q=q,
            debug=debug,
        )
    ).parsed

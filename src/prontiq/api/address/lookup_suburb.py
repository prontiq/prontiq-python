from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.address_debug_query import AddressDebugQuery
from ...models.address_error_response import AddressErrorResponse
from ...models.suburb_lookup_response import SuburbLookupResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    suburb: str,
    state: str | Unset = UNSET,
    limit: int | Unset = 10,
    debug: AddressDebugQuery | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["suburb"] = suburb

    params["state"] = state

    params["limit"] = limit

    json_debug: str | Unset = UNSET
    if not isinstance(debug, Unset):
        json_debug = debug

    params["debug"] = json_debug

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/address/lookup/suburb",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AddressErrorResponse | SuburbLookupResponse | None:
    if response.status_code == 200:
        response_200 = SuburbLookupResponse.from_dict(response.json())

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
) -> Response[AddressErrorResponse | SuburbLookupResponse]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    suburb: str,
    state: str | Unset = UNSET,
    limit: int | Unset = 10,
    debug: AddressDebugQuery | Unset = UNSET,
) -> Response[AddressErrorResponse | SuburbLookupResponse]:
    """Look up postcodes by suburb

     Find postcodes for an Australian suburb or locality. Add `state` to disambiguate common locality
    names that exist in multiple states. Responses may include an approximate bounding box and total
    address count.

    Args:
        suburb (str): Suburb/locality name. Example: sydney.
        state (str | Unset): Australian state or territory filter. Allowed values are `NSW`,
            `VIC`, `QLD`, `SA`, `WA`, `TAS`, `NT`, `ACT`, and `OT`. Input is case-insensitive and
            responses normalize state codes to uppercase. Example: QLD.
        limit (int | Unset): Maximum number of postcodes to return. Default: 10. Example: 3.
        debug (AddressDebugQuery | Unset): Optional diagnostic flag. Send exactly `true` or
            `false`. Invalid values are rejected; debug diagnostics are for support only and must not
            be used for business decisions. Example: false.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddressErrorResponse | SuburbLookupResponse]
    """

    kwargs = _get_kwargs(
        suburb=suburb,
        state=state,
        limit=limit,
        debug=debug,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    suburb: str,
    state: str | Unset = UNSET,
    limit: int | Unset = 10,
    debug: AddressDebugQuery | Unset = UNSET,
) -> AddressErrorResponse | SuburbLookupResponse | None:
    """Look up postcodes by suburb

     Find postcodes for an Australian suburb or locality. Add `state` to disambiguate common locality
    names that exist in multiple states. Responses may include an approximate bounding box and total
    address count.

    Args:
        suburb (str): Suburb/locality name. Example: sydney.
        state (str | Unset): Australian state or territory filter. Allowed values are `NSW`,
            `VIC`, `QLD`, `SA`, `WA`, `TAS`, `NT`, `ACT`, and `OT`. Input is case-insensitive and
            responses normalize state codes to uppercase. Example: QLD.
        limit (int | Unset): Maximum number of postcodes to return. Default: 10. Example: 3.
        debug (AddressDebugQuery | Unset): Optional diagnostic flag. Send exactly `true` or
            `false`. Invalid values are rejected; debug diagnostics are for support only and must not
            be used for business decisions. Example: false.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddressErrorResponse | SuburbLookupResponse
    """

    return sync_detailed(
        client=client,
        suburb=suburb,
        state=state,
        limit=limit,
        debug=debug,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    suburb: str,
    state: str | Unset = UNSET,
    limit: int | Unset = 10,
    debug: AddressDebugQuery | Unset = UNSET,
) -> Response[AddressErrorResponse | SuburbLookupResponse]:
    """Look up postcodes by suburb

     Find postcodes for an Australian suburb or locality. Add `state` to disambiguate common locality
    names that exist in multiple states. Responses may include an approximate bounding box and total
    address count.

    Args:
        suburb (str): Suburb/locality name. Example: sydney.
        state (str | Unset): Australian state or territory filter. Allowed values are `NSW`,
            `VIC`, `QLD`, `SA`, `WA`, `TAS`, `NT`, `ACT`, and `OT`. Input is case-insensitive and
            responses normalize state codes to uppercase. Example: QLD.
        limit (int | Unset): Maximum number of postcodes to return. Default: 10. Example: 3.
        debug (AddressDebugQuery | Unset): Optional diagnostic flag. Send exactly `true` or
            `false`. Invalid values are rejected; debug diagnostics are for support only and must not
            be used for business decisions. Example: false.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddressErrorResponse | SuburbLookupResponse]
    """

    kwargs = _get_kwargs(
        suburb=suburb,
        state=state,
        limit=limit,
        debug=debug,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    suburb: str,
    state: str | Unset = UNSET,
    limit: int | Unset = 10,
    debug: AddressDebugQuery | Unset = UNSET,
) -> AddressErrorResponse | SuburbLookupResponse | None:
    """Look up postcodes by suburb

     Find postcodes for an Australian suburb or locality. Add `state` to disambiguate common locality
    names that exist in multiple states. Responses may include an approximate bounding box and total
    address count.

    Args:
        suburb (str): Suburb/locality name. Example: sydney.
        state (str | Unset): Australian state or territory filter. Allowed values are `NSW`,
            `VIC`, `QLD`, `SA`, `WA`, `TAS`, `NT`, `ACT`, and `OT`. Input is case-insensitive and
            responses normalize state codes to uppercase. Example: QLD.
        limit (int | Unset): Maximum number of postcodes to return. Default: 10. Example: 3.
        debug (AddressDebugQuery | Unset): Optional diagnostic flag. Send exactly `true` or
            `false`. Invalid values are rejected; debug diagnostics are for support only and must not
            be used for business decisions. Example: false.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddressErrorResponse | SuburbLookupResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            suburb=suburb,
            state=state,
            limit=limit,
            debug=debug,
        )
    ).parsed

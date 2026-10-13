from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.address_debug_query import AddressDebugQuery
from ...models.address_error_response import AddressErrorResponse
from ...models.postcode_lookup_response import PostcodeLookupResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    postcode: str,
    limit: int | Unset = 10,
    debug: AddressDebugQuery | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["postcode"] = postcode

    params["limit"] = limit

    json_debug: str | Unset = UNSET
    if not isinstance(debug, Unset):
        json_debug = debug

    params["debug"] = json_debug

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/address/lookup/postcode",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AddressErrorResponse | PostcodeLookupResponse | None:
    if response.status_code == 200:
        response_200 = PostcodeLookupResponse.from_dict(response.json())

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
) -> Response[AddressErrorResponse | PostcodeLookupResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    postcode: str,
    limit: int | Unset = 10,
    debug: AddressDebugQuery | Unset = UNSET,
) -> Response[AddressErrorResponse | PostcodeLookupResponse]:
    """Look up localities by postcode

     List suburbs or localities that have address records in a four-digit Australian postcode. Use this
    for postcode-first forms, locality dropdowns, and coverage checks. `address_count` is dataset
    cardinality, not billing usage.

    Args:
        postcode (str): Australian 4-digit postcode. Example: 2000.
        limit (int | Unset): Maximum number of localities to return. Default: 10. Example: 3.
        debug (AddressDebugQuery | Unset): Optional diagnostic flag. Send exactly `true` or
            `false`. Invalid values are rejected; debug diagnostics are for support only and must not
            be used for business decisions. Example: false.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddressErrorResponse | PostcodeLookupResponse]
    """

    kwargs = _get_kwargs(
        postcode=postcode,
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
    postcode: str,
    limit: int | Unset = 10,
    debug: AddressDebugQuery | Unset = UNSET,
) -> AddressErrorResponse | PostcodeLookupResponse | None:
    """Look up localities by postcode

     List suburbs or localities that have address records in a four-digit Australian postcode. Use this
    for postcode-first forms, locality dropdowns, and coverage checks. `address_count` is dataset
    cardinality, not billing usage.

    Args:
        postcode (str): Australian 4-digit postcode. Example: 2000.
        limit (int | Unset): Maximum number of localities to return. Default: 10. Example: 3.
        debug (AddressDebugQuery | Unset): Optional diagnostic flag. Send exactly `true` or
            `false`. Invalid values are rejected; debug diagnostics are for support only and must not
            be used for business decisions. Example: false.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddressErrorResponse | PostcodeLookupResponse
    """

    return sync_detailed(
        client=client,
        postcode=postcode,
        limit=limit,
        debug=debug,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    postcode: str,
    limit: int | Unset = 10,
    debug: AddressDebugQuery | Unset = UNSET,
) -> Response[AddressErrorResponse | PostcodeLookupResponse]:
    """Look up localities by postcode

     List suburbs or localities that have address records in a four-digit Australian postcode. Use this
    for postcode-first forms, locality dropdowns, and coverage checks. `address_count` is dataset
    cardinality, not billing usage.

    Args:
        postcode (str): Australian 4-digit postcode. Example: 2000.
        limit (int | Unset): Maximum number of localities to return. Default: 10. Example: 3.
        debug (AddressDebugQuery | Unset): Optional diagnostic flag. Send exactly `true` or
            `false`. Invalid values are rejected; debug diagnostics are for support only and must not
            be used for business decisions. Example: false.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddressErrorResponse | PostcodeLookupResponse]
    """

    kwargs = _get_kwargs(
        postcode=postcode,
        limit=limit,
        debug=debug,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    postcode: str,
    limit: int | Unset = 10,
    debug: AddressDebugQuery | Unset = UNSET,
) -> AddressErrorResponse | PostcodeLookupResponse | None:
    """Look up localities by postcode

     List suburbs or localities that have address records in a four-digit Australian postcode. Use this
    for postcode-first forms, locality dropdowns, and coverage checks. `address_count` is dataset
    cardinality, not billing usage.

    Args:
        postcode (str): Australian 4-digit postcode. Example: 2000.
        limit (int | Unset): Maximum number of localities to return. Default: 10. Example: 3.
        debug (AddressDebugQuery | Unset): Optional diagnostic flag. Send exactly `true` or
            `false`. Invalid values are rejected; debug diagnostics are for support only and must not
            be used for business decisions. Example: false.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddressErrorResponse | PostcodeLookupResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            postcode=postcode,
            limit=limit,
            debug=debug,
        )
    ).parsed

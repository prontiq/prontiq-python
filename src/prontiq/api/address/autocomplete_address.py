from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.address_debug_query import AddressDebugQuery
from ...models.address_error_response import AddressErrorResponse
from ...models.autocomplete_address_response import AutocompleteAddressResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    q: str,
    state: str | Unset = UNSET,
    limit: int | Unset = 5,
    debug: AddressDebugQuery | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["q"] = q

    params["state"] = state

    params["limit"] = limit

    json_debug: str | Unset = UNSET
    if not isinstance(debug, Unset):
        json_debug = debug

    params["debug"] = json_debug

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/address/autocomplete",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AddressErrorResponse | AutocompleteAddressResponse | None:
    if response.status_code == 200:
        response_200 = AutocompleteAddressResponse.from_dict(response.json())

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
) -> Response[AddressErrorResponse | AutocompleteAddressResponse]:
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
    state: str | Unset = UNSET,
    limit: int | Unset = 5,
    debug: AddressDebugQuery | Unset = UNSET,
) -> Response[AddressErrorResponse | AutocompleteAddressResponse]:
    """Autocomplete addresses

     Suggest Australian addresses as a user types. Use this endpoint for typeahead UI flows, then pass
    the selected `id` to [Enrich](/api-reference/enrich) when you need coordinates, boundaries, and full
    record metadata. Suggestions include Prontiq match-quality fields; G-NAF confidence and internal
    search relevance are omitted from default responses.

    Args:
        q (str): Partial address text typed by the user. Send 1-200 characters; omit coordinates
            and use `state` when you already know the state. Example: 9 endeavour cou.
        state (str | Unset): Australian state or territory filter. Allowed values are `NSW`,
            `VIC`, `QLD`, `SA`, `WA`, `TAS`, `NT`, `ACT`, and `OT`. Input is case-insensitive and
            responses normalize state codes to uppercase. Example: QLD.
        limit (int | Unset): Maximum number of suggestions to return. Default: 5. Example: 3.
        debug (AddressDebugQuery | Unset): Optional diagnostic flag. Send exactly `true` or
            `false`. Invalid values are rejected; debug diagnostics are for support only and must not
            be used for business decisions. Example: false.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddressErrorResponse | AutocompleteAddressResponse]
    """

    kwargs = _get_kwargs(
        q=q,
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
    q: str,
    state: str | Unset = UNSET,
    limit: int | Unset = 5,
    debug: AddressDebugQuery | Unset = UNSET,
) -> AddressErrorResponse | AutocompleteAddressResponse | None:
    """Autocomplete addresses

     Suggest Australian addresses as a user types. Use this endpoint for typeahead UI flows, then pass
    the selected `id` to [Enrich](/api-reference/enrich) when you need coordinates, boundaries, and full
    record metadata. Suggestions include Prontiq match-quality fields; G-NAF confidence and internal
    search relevance are omitted from default responses.

    Args:
        q (str): Partial address text typed by the user. Send 1-200 characters; omit coordinates
            and use `state` when you already know the state. Example: 9 endeavour cou.
        state (str | Unset): Australian state or territory filter. Allowed values are `NSW`,
            `VIC`, `QLD`, `SA`, `WA`, `TAS`, `NT`, `ACT`, and `OT`. Input is case-insensitive and
            responses normalize state codes to uppercase. Example: QLD.
        limit (int | Unset): Maximum number of suggestions to return. Default: 5. Example: 3.
        debug (AddressDebugQuery | Unset): Optional diagnostic flag. Send exactly `true` or
            `false`. Invalid values are rejected; debug diagnostics are for support only and must not
            be used for business decisions. Example: false.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddressErrorResponse | AutocompleteAddressResponse
    """

    return sync_detailed(
        client=client,
        q=q,
        state=state,
        limit=limit,
        debug=debug,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    q: str,
    state: str | Unset = UNSET,
    limit: int | Unset = 5,
    debug: AddressDebugQuery | Unset = UNSET,
) -> Response[AddressErrorResponse | AutocompleteAddressResponse]:
    """Autocomplete addresses

     Suggest Australian addresses as a user types. Use this endpoint for typeahead UI flows, then pass
    the selected `id` to [Enrich](/api-reference/enrich) when you need coordinates, boundaries, and full
    record metadata. Suggestions include Prontiq match-quality fields; G-NAF confidence and internal
    search relevance are omitted from default responses.

    Args:
        q (str): Partial address text typed by the user. Send 1-200 characters; omit coordinates
            and use `state` when you already know the state. Example: 9 endeavour cou.
        state (str | Unset): Australian state or territory filter. Allowed values are `NSW`,
            `VIC`, `QLD`, `SA`, `WA`, `TAS`, `NT`, `ACT`, and `OT`. Input is case-insensitive and
            responses normalize state codes to uppercase. Example: QLD.
        limit (int | Unset): Maximum number of suggestions to return. Default: 5. Example: 3.
        debug (AddressDebugQuery | Unset): Optional diagnostic flag. Send exactly `true` or
            `false`. Invalid values are rejected; debug diagnostics are for support only and must not
            be used for business decisions. Example: false.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddressErrorResponse | AutocompleteAddressResponse]
    """

    kwargs = _get_kwargs(
        q=q,
        state=state,
        limit=limit,
        debug=debug,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    q: str,
    state: str | Unset = UNSET,
    limit: int | Unset = 5,
    debug: AddressDebugQuery | Unset = UNSET,
) -> AddressErrorResponse | AutocompleteAddressResponse | None:
    """Autocomplete addresses

     Suggest Australian addresses as a user types. Use this endpoint for typeahead UI flows, then pass
    the selected `id` to [Enrich](/api-reference/enrich) when you need coordinates, boundaries, and full
    record metadata. Suggestions include Prontiq match-quality fields; G-NAF confidence and internal
    search relevance are omitted from default responses.

    Args:
        q (str): Partial address text typed by the user. Send 1-200 characters; omit coordinates
            and use `state` when you already know the state. Example: 9 endeavour cou.
        state (str | Unset): Australian state or territory filter. Allowed values are `NSW`,
            `VIC`, `QLD`, `SA`, `WA`, `TAS`, `NT`, `ACT`, and `OT`. Input is case-insensitive and
            responses normalize state codes to uppercase. Example: QLD.
        limit (int | Unset): Maximum number of suggestions to return. Default: 5. Example: 3.
        debug (AddressDebugQuery | Unset): Optional diagnostic flag. Send exactly `true` or
            `false`. Invalid values are rejected; debug diagnostics are for support only and must not
            be used for business decisions. Example: false.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddressErrorResponse | AutocompleteAddressResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            q=q,
            state=state,
            limit=limit,
            debug=debug,
        )
    ).parsed

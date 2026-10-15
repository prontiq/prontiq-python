from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.address_debug_query import AddressDebugQuery
from ...models.address_error_response import AddressErrorResponse
from ...models.reverse_geocode_address_response import ReverseGeocodeAddressResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    lat: float,
    lon: float,
    radius: float | Unset = 100.0,
    limit: int | Unset = 5,
    debug: AddressDebugQuery | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["lat"] = lat

    params["lon"] = lon

    params["radius"] = radius

    params["limit"] = limit

    json_debug: str | Unset = UNSET
    if not isinstance(debug, Unset):
        json_debug = debug

    params["debug"] = json_debug

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/v1/address/reverse",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> AddressErrorResponse | ReverseGeocodeAddressResponse | None:
    if response.status_code == 200:
        response_200 = ReverseGeocodeAddressResponse.from_dict(response.json())

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
) -> Response[AddressErrorResponse | ReverseGeocodeAddressResponse]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    lat: float,
    lon: float,
    radius: float | Unset = 100.0,
    limit: int | Unset = 5,
    debug: AddressDebugQuery | Unset = UNSET,
) -> Response[AddressErrorResponse | ReverseGeocodeAddressResponse]:
    """Reverse geocode nearby addresses

     Find addresses near a latitude and longitude. Use this when a workflow starts from a map pin, device
    coordinate, or spatial search. Results are ordered by distance and include `distance_m` in metres.

    Args:
        lat (float): Latitude in GDA2020 (EPSG:7844) decimal degrees for the reverse-geocode
            search point. Example: -23.1601.
        lon (float): Longitude in GDA2020 (EPSG:7844) decimal degrees for the reverse-geocode
            search point. Example: 150.7596.
        radius (float | Unset): Search radius in metres. Default: 100.0. Example: 200.
        limit (int | Unset): Maximum number of nearby addresses to return. Default: 5. Example: 3.
        debug (AddressDebugQuery | Unset): Optional diagnostic flag. Send exactly `true` or
            `false`. Invalid values are rejected; debug diagnostics are for support only and must not
            be used for business decisions. Example: false.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddressErrorResponse | ReverseGeocodeAddressResponse]
    """

    kwargs = _get_kwargs(
        lat=lat,
        lon=lon,
        radius=radius,
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
    lat: float,
    lon: float,
    radius: float | Unset = 100.0,
    limit: int | Unset = 5,
    debug: AddressDebugQuery | Unset = UNSET,
) -> AddressErrorResponse | ReverseGeocodeAddressResponse | None:
    """Reverse geocode nearby addresses

     Find addresses near a latitude and longitude. Use this when a workflow starts from a map pin, device
    coordinate, or spatial search. Results are ordered by distance and include `distance_m` in metres.

    Args:
        lat (float): Latitude in GDA2020 (EPSG:7844) decimal degrees for the reverse-geocode
            search point. Example: -23.1601.
        lon (float): Longitude in GDA2020 (EPSG:7844) decimal degrees for the reverse-geocode
            search point. Example: 150.7596.
        radius (float | Unset): Search radius in metres. Default: 100.0. Example: 200.
        limit (int | Unset): Maximum number of nearby addresses to return. Default: 5. Example: 3.
        debug (AddressDebugQuery | Unset): Optional diagnostic flag. Send exactly `true` or
            `false`. Invalid values are rejected; debug diagnostics are for support only and must not
            be used for business decisions. Example: false.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddressErrorResponse | ReverseGeocodeAddressResponse
    """

    return sync_detailed(
        client=client,
        lat=lat,
        lon=lon,
        radius=radius,
        limit=limit,
        debug=debug,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    lat: float,
    lon: float,
    radius: float | Unset = 100.0,
    limit: int | Unset = 5,
    debug: AddressDebugQuery | Unset = UNSET,
) -> Response[AddressErrorResponse | ReverseGeocodeAddressResponse]:
    """Reverse geocode nearby addresses

     Find addresses near a latitude and longitude. Use this when a workflow starts from a map pin, device
    coordinate, or spatial search. Results are ordered by distance and include `distance_m` in metres.

    Args:
        lat (float): Latitude in GDA2020 (EPSG:7844) decimal degrees for the reverse-geocode
            search point. Example: -23.1601.
        lon (float): Longitude in GDA2020 (EPSG:7844) decimal degrees for the reverse-geocode
            search point. Example: 150.7596.
        radius (float | Unset): Search radius in metres. Default: 100.0. Example: 200.
        limit (int | Unset): Maximum number of nearby addresses to return. Default: 5. Example: 3.
        debug (AddressDebugQuery | Unset): Optional diagnostic flag. Send exactly `true` or
            `false`. Invalid values are rejected; debug diagnostics are for support only and must not
            be used for business decisions. Example: false.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AddressErrorResponse | ReverseGeocodeAddressResponse]
    """

    kwargs = _get_kwargs(
        lat=lat,
        lon=lon,
        radius=radius,
        limit=limit,
        debug=debug,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    lat: float,
    lon: float,
    radius: float | Unset = 100.0,
    limit: int | Unset = 5,
    debug: AddressDebugQuery | Unset = UNSET,
) -> AddressErrorResponse | ReverseGeocodeAddressResponse | None:
    """Reverse geocode nearby addresses

     Find addresses near a latitude and longitude. Use this when a workflow starts from a map pin, device
    coordinate, or spatial search. Results are ordered by distance and include `distance_m` in metres.

    Args:
        lat (float): Latitude in GDA2020 (EPSG:7844) decimal degrees for the reverse-geocode
            search point. Example: -23.1601.
        lon (float): Longitude in GDA2020 (EPSG:7844) decimal degrees for the reverse-geocode
            search point. Example: 150.7596.
        radius (float | Unset): Search radius in metres. Default: 100.0. Example: 200.
        limit (int | Unset): Maximum number of nearby addresses to return. Default: 5. Example: 3.
        debug (AddressDebugQuery | Unset): Optional diagnostic flag. Send exactly `true` or
            `false`. Invalid values are rejected; debug diagnostics are for support only and must not
            be used for business decisions. Example: false.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AddressErrorResponse | ReverseGeocodeAddressResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            lat=lat,
            lon=lon,
            radius=radius,
            limit=limit,
            debug=debug,
        )
    ).parsed

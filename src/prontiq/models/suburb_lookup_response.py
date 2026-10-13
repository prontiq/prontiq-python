from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.australian_state_code import (
    AustralianStateCode,
    check_australian_state_code,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.debug_info import DebugInfo
    from ..models.geo_bounds import GeoBounds


T = TypeVar("T", bound="SuburbLookupResponse")


@_attrs_define
class SuburbLookupResponse:
    """Postcodes, bounds, and address count for a suburb or locality.

    Attributes:
        suburb (str): Normalized suburb or locality name returned in uppercase. Example: SYDNEY.
        postcodes (list[str]): Postcodes associated with this suburb or locality. Example: ['2000'].
        address_count (int): Total address records in this suburb or locality. This is dataset cardinality, not credit
            usage. Example: 12345.
        state (AustralianStateCode | None | Unset): Australian state or territory used to disambiguate the locality when
            available. The value is uppercase in responses. Example: NSW.
        bounds (GeoBounds | Unset): Approximate bounding box for the suburb or locality when available. Example:
            {'top_left': {'lat': -33.8568, 'lon': 151.2001}, 'bottom_right': {'lat': -33.8812, 'lon': 151.2204}}.
        debug (DebugInfo | Unset): Optional diagnostic metadata returned only when `debug=true` is supplied. Debug
            values are for support and troubleshooting, not production decision-making. Example: {'scoringVersion':
            'address-match-v1', 'queryMode': 'autocomplete', 'searchScore': 42.1}.
    """

    suburb: str
    postcodes: list[str]
    address_count: int
    state: AustralianStateCode | None | Unset = UNSET
    bounds: GeoBounds | Unset = UNSET
    debug: DebugInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        suburb = self.suburb

        postcodes = self.postcodes

        address_count = self.address_count

        state: None | str | Unset
        if isinstance(self.state, Unset):
            state = UNSET
        elif isinstance(self.state, str):
            state = self.state
        else:
            state = self.state

        bounds: dict[str, Any] | Unset = UNSET
        if not isinstance(self.bounds, Unset):
            bounds = self.bounds.to_dict()

        debug: dict[str, Any] | Unset = UNSET
        if not isinstance(self.debug, Unset):
            debug = self.debug.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "suburb": suburb,
                "postcodes": postcodes,
                "address_count": address_count,
            }
        )
        if state is not UNSET:
            field_dict["state"] = state
        if bounds is not UNSET:
            field_dict["bounds"] = bounds
        if debug is not UNSET:
            field_dict["debug"] = debug

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.debug_info import DebugInfo  # noqa: PLC0415
        from ..models.geo_bounds import GeoBounds  # noqa: PLC0415

        d = dict(src_dict)
        suburb = d.pop("suburb")

        postcodes = cast(list[str], d.pop("postcodes"))

        address_count = d.pop("address_count")

        def _parse_state(data: object) -> AustralianStateCode | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                state_type_0 = check_australian_state_code(data)

                return state_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AustralianStateCode | None | Unset, data)

        state = _parse_state(d.pop("state", UNSET))

        _bounds = d.pop("bounds", UNSET)
        bounds: GeoBounds | Unset
        if isinstance(_bounds, Unset):
            bounds = UNSET
        else:
            bounds = GeoBounds.from_dict(_bounds)

        _debug = d.pop("debug", UNSET)
        debug: DebugInfo | Unset
        if isinstance(_debug, Unset):
            debug = UNSET
        else:
            debug = DebugInfo.from_dict(_debug)

        suburb_lookup_response = cls(
            suburb=suburb,
            postcodes=postcodes,
            address_count=address_count,
            state=state,
            bounds=bounds,
            debug=debug,
        )

        suburb_lookup_response.additional_properties = d
        return suburb_lookup_response

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

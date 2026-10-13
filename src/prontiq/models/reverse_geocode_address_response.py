from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.debug_info import DebugInfo
    from ..models.reverse_address_result import ReverseAddressResult


T = TypeVar("T", bound="ReverseGeocodeAddressResponse")


@_attrs_define
class ReverseGeocodeAddressResponse:
    """Addresses nearest to the supplied latitude and longitude.

    Attributes:
        results (list[ReverseAddressResult]): Nearby address documents sorted by distance from the submitted coordinate.
            The array may be empty when no address falls within the radius.
        total (int): Total address records found within the requested radius. Example: 1.
        debug (DebugInfo | Unset): Optional diagnostic metadata returned only when `debug=true` is supplied. Debug
            values are for support and troubleshooting, not production decision-making. Example: {'scoringVersion':
            'address-match-v1', 'queryMode': 'autocomplete', 'searchScore': 42.1}.
    """

    results: list[ReverseAddressResult]
    total: int
    debug: DebugInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        total = self.total

        debug: dict[str, Any] | Unset = UNSET
        if not isinstance(self.debug, Unset):
            debug = self.debug.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "results": results,
                "total": total,
            }
        )
        if debug is not UNSET:
            field_dict["debug"] = debug

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.debug_info import DebugInfo  # noqa: PLC0415
        from ..models.reverse_address_result import (
            ReverseAddressResult,  # noqa: PLC0415
        )

        d = dict(src_dict)
        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = ReverseAddressResult.from_dict(results_item_data)

            results.append(results_item)

        total = d.pop("total")

        _debug = d.pop("debug", UNSET)
        debug: DebugInfo | Unset
        if isinstance(_debug, Unset):
            debug = UNSET
        else:
            debug = DebugInfo.from_dict(_debug)

        reverse_geocode_address_response = cls(
            results=results,
            total=total,
            debug=debug,
        )

        reverse_geocode_address_response.additional_properties = d
        return reverse_geocode_address_response

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

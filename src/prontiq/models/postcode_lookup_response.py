from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.debug_info import DebugInfo
    from ..models.postcode_locality_summary import PostcodeLocalitySummary


T = TypeVar("T", bound="PostcodeLookupResponse")


@_attrs_define
class PostcodeLookupResponse:
    """Localities and address counts for an Australian postcode.

    Attributes:
        postcode (str): Four-digit Australian postcode. Store postcodes as strings; integer coercion can remove leading
            zeroes used by some Australian postcodes. Example: 4703.
        localities (list[PostcodeLocalitySummary]): Localities that contain address records for the requested postcode,
            ordered by the lookup implementation. Example: [{'name': 'SYDNEY', 'state': 'NSW', 'address_count': 12345}].
        debug (DebugInfo | Unset): Optional diagnostic metadata returned only when `debug=true` is supplied. Debug
            values are for support and troubleshooting, not production decision-making. Example: {'scoringVersion':
            'address-match-v1', 'queryMode': 'autocomplete', 'searchScore': 42.1}.
    """

    postcode: str
    localities: list[PostcodeLocalitySummary]
    debug: DebugInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        postcode = self.postcode

        localities = []
        for localities_item_data in self.localities:
            localities_item = localities_item_data.to_dict()
            localities.append(localities_item)

        debug: dict[str, Any] | Unset = UNSET
        if not isinstance(self.debug, Unset):
            debug = self.debug.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "postcode": postcode,
                "localities": localities,
            }
        )
        if debug is not UNSET:
            field_dict["debug"] = debug

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.debug_info import DebugInfo  # noqa: PLC0415
        from ..models.postcode_locality_summary import (
            PostcodeLocalitySummary,  # noqa: PLC0415
        )

        d = dict(src_dict)
        postcode = d.pop("postcode")

        localities = []
        _localities = d.pop("localities")
        for localities_item_data in _localities:
            localities_item = PostcodeLocalitySummary.from_dict(localities_item_data)

            localities.append(localities_item)

        _debug = d.pop("debug", UNSET)
        debug: DebugInfo | Unset
        if isinstance(_debug, Unset):
            debug = UNSET
        else:
            debug = DebugInfo.from_dict(_debug)

        postcode_lookup_response = cls(
            postcode=postcode,
            localities=localities,
            debug=debug,
        )

        postcode_lookup_response.additional_properties = d
        return postcode_lookup_response

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

from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.location import Location


T = TypeVar("T", bound="GeoBounds")


@_attrs_define
class GeoBounds:
    """Approximate bounding box for the suburb or locality when available.

    Example:
        {'top_left': {'lat': -33.8568, 'lon': 151.2001}, 'bottom_right': {'lat': -33.8812, 'lon': 151.2204}}

    Attributes:
        top_left (Location): Compact latitude/longitude point used for proximity workflows and map display. Example:
            {'lat': -23.1601, 'lon': 150.7596}.
        bottom_right (Location): Compact latitude/longitude point used for proximity workflows and map display. Example:
            {'lat': -23.1601, 'lon': 150.7596}.
    """

    top_left: Location
    bottom_right: Location
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        top_left = self.top_left.to_dict()

        bottom_right = self.bottom_right.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "top_left": top_left,
                "bottom_right": bottom_right,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.location import Location  # noqa: PLC0415

        d = dict(src_dict)
        top_left = Location.from_dict(d.pop("top_left"))

        bottom_right = Location.from_dict(d.pop("bottom_right"))

        geo_bounds = cls(
            top_left=top_left,
            bottom_right=bottom_right,
        )

        geo_bounds.additional_properties = d
        return geo_bounds

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

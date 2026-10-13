from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.debug_info_matched_components_additional_property import (
    DebugInfoMatchedComponentsAdditionalProperty,
    check_debug_info_matched_components_additional_property,
)

T = TypeVar("T", bound="DebugInfoMatchedComponents")


@_attrs_define
class DebugInfoMatchedComponents:
    """Per-component match classification for diagnostics. Shape may evolve between scoring versions.

    Example:
        {'streetNumber': 'exact', 'streetName': 'prefix', 'locality': 'exact'}

    """

    additional_properties: dict[str, DebugInfoMatchedComponentsAdditionalProperty] = (
        _attrs_field(init=False, factory=dict)
    )

    def to_dict(self) -> dict[str, Any]:

        field_dict: dict[str, Any] = {}
        for prop_name, prop in self.additional_properties.items():
            field_dict[prop_name] = prop

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        debug_info_matched_components = cls()

        additional_properties = {}
        for prop_name, prop_dict in d.items():
            additional_property = (
                check_debug_info_matched_components_additional_property(prop_dict)
            )

            additional_properties[prop_name] = additional_property

        debug_info_matched_components.additional_properties = additional_properties
        return debug_info_matched_components

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> DebugInfoMatchedComponentsAdditionalProperty:
        return self.additional_properties[key]

    def __setitem__(
        self, key: str, value: DebugInfoMatchedComponentsAdditionalProperty
    ) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StreetContext")


@_attrs_define
class StreetContext:
    """Street context when available for the enriched address.

    Example:
        {'id': 'VIC1953679', 'classification': 'CONFIRMED', 'aliases': []}

    Attributes:
        id (None | str | Unset):
        classification (None | str | Unset):
        aliases (list[str] | Unset): Alternative street names when available. Example: ['OLD DUKE STREET'].
    """

    id: None | str | Unset = UNSET
    classification: None | str | Unset = UNSET
    aliases: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id: None | str | Unset
        if isinstance(self.id, Unset):
            id = UNSET
        else:
            id = self.id

        classification: None | str | Unset
        if isinstance(self.classification, Unset):
            classification = UNSET
        else:
            classification = self.classification

        aliases: list[str] | Unset = UNSET
        if not isinstance(self.aliases, Unset):
            aliases = self.aliases

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if classification is not UNSET:
            field_dict["classification"] = classification
        if aliases is not UNSET:
            field_dict["aliases"] = aliases

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        id = _parse_id(d.pop("id", UNSET))

        def _parse_classification(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        classification = _parse_classification(d.pop("classification", UNSET))

        aliases = cast(list[str], d.pop("aliases", UNSET))

        street_context = cls(
            id=id,
            classification=classification,
            aliases=aliases,
        )

        street_context.additional_properties = d
        return street_context

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

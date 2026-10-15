from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="LocalityContext")


@_attrs_define
class LocalityContext:
    """Locality context when available for the enriched address.

    Example:
        {'id': 'loc1b5a0e70afd4', 'classification': 'GAZETTED LOCALITY', 'neighbours': ['ELSTERNWICK', 'GARDENVALE',
            'ORMOND'], 'aliases': []}

    Attributes:
        id (None | str | Unset):
        classification (None | str | Unset):
        neighbours (list[str] | Unset): Neighbouring locality names when available. Example: ['ELSTERNWICK',
            'GARDENVALE', 'ORMOND'].
        aliases (list[str] | Unset): Alternative locality names when available. Example: ['FOOTSCRAY WEST'].
    """

    id: None | str | Unset = UNSET
    classification: None | str | Unset = UNSET
    neighbours: list[str] | Unset = UNSET
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

        neighbours: list[str] | Unset = UNSET
        if not isinstance(self.neighbours, Unset):
            neighbours = self.neighbours

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
        if neighbours is not UNSET:
            field_dict["neighbours"] = neighbours
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

        neighbours = cast(list[str], d.pop("neighbours", UNSET))

        aliases = cast(list[str], d.pop("aliases", UNSET))

        locality_context = cls(
            id=id,
            classification=classification,
            neighbours=neighbours,
            aliases=aliases,
        )

        locality_context.additional_properties = d
        return locality_context

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

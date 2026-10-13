from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validate_address_response_prontiq_match_quality import (
    ValidateAddressResponseProntiqMatchQuality,
    check_validate_address_response_prontiq_match_quality,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.address_document import AddressDocument
    from ..models.debug_info import DebugInfo


T = TypeVar("T", bound="ValidateAddressResponse")


@_attrs_define
class ValidateAddressResponse:
    """Best address match and Prontiq match-quality classification for a submitted address string.

    Attributes:
        match (AddressDocument | None): Best matching full address document, or `null` when the submitted address does
            not resolve to a usable G-NAF record.
        prontiq_match_score (int): Prontiq-computed request match score from 0 to 100. Use it to decide whether to
            accept the match, ask the user to confirm, or request correction. Example: 92.
        prontiq_match_quality (ValidateAddressResponseProntiqMatchQuality): Human-readable Prontiq match-quality bucket
            derived from `prontiqMatchScore`. This is distinct from `match.confidence`, which is G-NAF source-record
            metadata. Example: high.
        debug (DebugInfo | Unset): Optional diagnostic metadata returned only when `debug=true` is supplied. Debug
            values are for support and troubleshooting, not production decision-making. Example: {'scoringVersion':
            'address-match-v1', 'queryMode': 'autocomplete', 'searchScore': 42.1}.
    """

    match: AddressDocument | None
    prontiq_match_score: int
    prontiq_match_quality: ValidateAddressResponseProntiqMatchQuality
    debug: DebugInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.address_document import AddressDocument  # noqa: PLC0415

        match: dict[str, Any] | None
        if isinstance(self.match, AddressDocument):
            match = self.match.to_dict()
        else:
            match = self.match

        prontiq_match_score = self.prontiq_match_score

        prontiq_match_quality: str = self.prontiq_match_quality

        debug: dict[str, Any] | Unset = UNSET
        if not isinstance(self.debug, Unset):
            debug = self.debug.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "match": match,
                "prontiqMatchScore": prontiq_match_score,
                "prontiqMatchQuality": prontiq_match_quality,
            }
        )
        if debug is not UNSET:
            field_dict["debug"] = debug

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.address_document import AddressDocument  # noqa: PLC0415
        from ..models.debug_info import DebugInfo  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_match(data: object) -> AddressDocument | None:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                match_type_0 = AddressDocument.from_dict(data)

                return match_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AddressDocument | None, data)

        match = _parse_match(d.pop("match"))

        prontiq_match_score = d.pop("prontiqMatchScore")

        prontiq_match_quality = check_validate_address_response_prontiq_match_quality(
            d.pop("prontiqMatchQuality")
        )

        _debug = d.pop("debug", UNSET)
        debug: DebugInfo | Unset
        if isinstance(_debug, Unset):
            debug = UNSET
        else:
            debug = DebugInfo.from_dict(_debug)

        validate_address_response = cls(
            match=match,
            prontiq_match_score=prontiq_match_score,
            prontiq_match_quality=prontiq_match_quality,
            debug=debug,
        )

        validate_address_response.additional_properties = d
        return validate_address_response

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

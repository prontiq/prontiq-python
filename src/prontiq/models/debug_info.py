from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.debug_info_query_mode import (
    DebugInfoQueryMode,
    check_debug_info_query_mode,
)
from ..models.debug_info_scoring_version import (
    DebugInfoScoringVersion,
    check_debug_info_scoring_version,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.debug_info_matched_components import DebugInfoMatchedComponents


T = TypeVar("T", bound="DebugInfo")


@_attrs_define
class DebugInfo:
    """Optional diagnostic metadata returned only when `debug=true` is supplied. Debug values are for support and
    troubleshooting, not production decision-making.

        Example:
            {'scoringVersion': 'address-match-v1', 'queryMode': 'autocomplete', 'searchScore': 42.1}

        Attributes:
            scoring_version (DebugInfoScoringVersion): Version of the public Prontiq match-scoring algorithm used for
                diagnostics. Example: address-match-v1.
            query_mode (DebugInfoQueryMode): Address API operation mode that produced this diagnostic object. Example:
                autocomplete.
            matched_components (DebugInfoMatchedComponents | Unset): Per-component match classification for diagnostics.
                Shape may evolve between scoring versions. Example: {'streetNumber': 'exact', 'streetName': 'prefix',
                'locality': 'exact'}.
            score_caps (list[str] | Unset): Diagnostic list of caps applied to the score, such as explicit postcode or state
                mismatches. Example: ['explicitPostcodeMismatch'].
            search_score (float | Unset): Internal search relevance score when available. This value is unstable and must
                not be stored, sorted by, or used for business decisions. Example: 42.1.
    """

    scoring_version: DebugInfoScoringVersion
    query_mode: DebugInfoQueryMode
    matched_components: DebugInfoMatchedComponents | Unset = UNSET
    score_caps: list[str] | Unset = UNSET
    search_score: float | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        scoring_version: str = self.scoring_version

        query_mode: str = self.query_mode

        matched_components: dict[str, Any] | Unset = UNSET
        if not isinstance(self.matched_components, Unset):
            matched_components = self.matched_components.to_dict()

        score_caps: list[str] | Unset = UNSET
        if not isinstance(self.score_caps, Unset):
            score_caps = self.score_caps

        search_score = self.search_score

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "scoringVersion": scoring_version,
                "queryMode": query_mode,
            }
        )
        if matched_components is not UNSET:
            field_dict["matchedComponents"] = matched_components
        if score_caps is not UNSET:
            field_dict["scoreCaps"] = score_caps
        if search_score is not UNSET:
            field_dict["searchScore"] = search_score

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.debug_info_matched_components import (
            DebugInfoMatchedComponents,  # noqa: PLC0415
        )

        d = dict(src_dict)
        scoring_version = check_debug_info_scoring_version(d.pop("scoringVersion"))

        query_mode = check_debug_info_query_mode(d.pop("queryMode"))

        _matched_components = d.pop("matchedComponents", UNSET)
        matched_components: DebugInfoMatchedComponents | Unset
        if isinstance(_matched_components, Unset):
            matched_components = UNSET
        else:
            matched_components = DebugInfoMatchedComponents.from_dict(
                _matched_components
            )

        score_caps = cast(list[str], d.pop("scoreCaps", UNSET))

        search_score = d.pop("searchScore", UNSET)

        debug_info = cls(
            scoring_version=scoring_version,
            query_mode=query_mode,
            matched_components=matched_components,
            score_caps=score_caps,
            search_score=search_score,
        )

        debug_info.additional_properties = d
        return debug_info

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

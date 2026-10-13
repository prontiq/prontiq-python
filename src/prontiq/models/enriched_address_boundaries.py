from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.mesh_block import MeshBlock
    from ..models.named_area import NamedArea
    from ..models.ward import Ward


T = TypeVar("T", bound="EnrichedAddressBoundaries")


@_attrs_define
class EnrichedAddressBoundaries:
    """Administrative, electoral, and ABS geography returned by Enrich. This is a strict superset of the standard address
    boundary object.

        Example:
            {'lga': {'name': 'Glen Eira', 'code': 'lga9bd137c30d17'}, 'ward': {'name': 'Bambra Ward'}, 'meshBlock': {'code':
                '20192490000', 'category': 'Residential'}, 'sa1': '20802117831', 'sa2': {'name': 'Caulfield - South', 'code':
                '208021178'}}

        Attributes:
            lga (NamedArea | None | Unset):
            state_electorate (NamedArea | None | Unset):
            commonwealth_electorate (NamedArea | None | Unset):
            mesh_block (MeshBlock | None | Unset):
            sa2 (NamedArea | None | Unset):
            sa3 (NamedArea | None | Unset):
            sa4 (NamedArea | None | Unset):
            gccsa (NamedArea | None | Unset):
            sa1 (None | str | Unset):
            ward (None | Unset | Ward):
    """

    lga: NamedArea | None | Unset = UNSET
    state_electorate: NamedArea | None | Unset = UNSET
    commonwealth_electorate: NamedArea | None | Unset = UNSET
    mesh_block: MeshBlock | None | Unset = UNSET
    sa2: NamedArea | None | Unset = UNSET
    sa3: NamedArea | None | Unset = UNSET
    sa4: NamedArea | None | Unset = UNSET
    gccsa: NamedArea | None | Unset = UNSET
    sa1: None | str | Unset = UNSET
    ward: None | Unset | Ward = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.mesh_block import MeshBlock  # noqa: PLC0415
        from ..models.named_area import NamedArea  # noqa: PLC0415
        from ..models.ward import Ward  # noqa: PLC0415

        lga: dict[str, Any] | None | Unset
        if isinstance(self.lga, Unset):
            lga = UNSET
        elif isinstance(self.lga, NamedArea):
            lga = self.lga.to_dict()
        else:
            lga = self.lga

        state_electorate: dict[str, Any] | None | Unset
        if isinstance(self.state_electorate, Unset):
            state_electorate = UNSET
        elif isinstance(self.state_electorate, NamedArea):
            state_electorate = self.state_electorate.to_dict()
        else:
            state_electorate = self.state_electorate

        commonwealth_electorate: dict[str, Any] | None | Unset
        if isinstance(self.commonwealth_electorate, Unset):
            commonwealth_electorate = UNSET
        elif isinstance(self.commonwealth_electorate, NamedArea):
            commonwealth_electorate = self.commonwealth_electorate.to_dict()
        else:
            commonwealth_electorate = self.commonwealth_electorate

        mesh_block: dict[str, Any] | None | Unset
        if isinstance(self.mesh_block, Unset):
            mesh_block = UNSET
        elif isinstance(self.mesh_block, MeshBlock):
            mesh_block = self.mesh_block.to_dict()
        else:
            mesh_block = self.mesh_block

        sa2: dict[str, Any] | None | Unset
        if isinstance(self.sa2, Unset):
            sa2 = UNSET
        elif isinstance(self.sa2, NamedArea):
            sa2 = self.sa2.to_dict()
        else:
            sa2 = self.sa2

        sa3: dict[str, Any] | None | Unset
        if isinstance(self.sa3, Unset):
            sa3 = UNSET
        elif isinstance(self.sa3, NamedArea):
            sa3 = self.sa3.to_dict()
        else:
            sa3 = self.sa3

        sa4: dict[str, Any] | None | Unset
        if isinstance(self.sa4, Unset):
            sa4 = UNSET
        elif isinstance(self.sa4, NamedArea):
            sa4 = self.sa4.to_dict()
        else:
            sa4 = self.sa4

        gccsa: dict[str, Any] | None | Unset
        if isinstance(self.gccsa, Unset):
            gccsa = UNSET
        elif isinstance(self.gccsa, NamedArea):
            gccsa = self.gccsa.to_dict()
        else:
            gccsa = self.gccsa

        sa1: None | str | Unset
        if isinstance(self.sa1, Unset):
            sa1 = UNSET
        else:
            sa1 = self.sa1

        ward: dict[str, Any] | None | Unset
        if isinstance(self.ward, Unset):
            ward = UNSET
        elif isinstance(self.ward, Ward):
            ward = self.ward.to_dict()
        else:
            ward = self.ward

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lga is not UNSET:
            field_dict["lga"] = lga
        if state_electorate is not UNSET:
            field_dict["stateElectorate"] = state_electorate
        if commonwealth_electorate is not UNSET:
            field_dict["commonwealthElectorate"] = commonwealth_electorate
        if mesh_block is not UNSET:
            field_dict["meshBlock"] = mesh_block
        if sa2 is not UNSET:
            field_dict["sa2"] = sa2
        if sa3 is not UNSET:
            field_dict["sa3"] = sa3
        if sa4 is not UNSET:
            field_dict["sa4"] = sa4
        if gccsa is not UNSET:
            field_dict["gccsa"] = gccsa
        if sa1 is not UNSET:
            field_dict["sa1"] = sa1
        if ward is not UNSET:
            field_dict["ward"] = ward

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.mesh_block import MeshBlock  # noqa: PLC0415
        from ..models.named_area import NamedArea  # noqa: PLC0415
        from ..models.ward import Ward  # noqa: PLC0415

        d = dict(src_dict)

        def _parse_lga(data: object) -> NamedArea | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                lga_type_0 = NamedArea.from_dict(data)

                return lga_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NamedArea | None | Unset, data)

        lga = _parse_lga(d.pop("lga", UNSET))

        def _parse_state_electorate(data: object) -> NamedArea | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                state_electorate_type_0 = NamedArea.from_dict(data)

                return state_electorate_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NamedArea | None | Unset, data)

        state_electorate = _parse_state_electorate(d.pop("stateElectorate", UNSET))

        def _parse_commonwealth_electorate(data: object) -> NamedArea | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                commonwealth_electorate_type_0 = NamedArea.from_dict(data)

                return commonwealth_electorate_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NamedArea | None | Unset, data)

        commonwealth_electorate = _parse_commonwealth_electorate(
            d.pop("commonwealthElectorate", UNSET)
        )

        def _parse_mesh_block(data: object) -> MeshBlock | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                mesh_block_type_0 = MeshBlock.from_dict(data)

                return mesh_block_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(MeshBlock | None | Unset, data)

        mesh_block = _parse_mesh_block(d.pop("meshBlock", UNSET))

        def _parse_sa2(data: object) -> NamedArea | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                sa2_type_0 = NamedArea.from_dict(data)

                return sa2_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NamedArea | None | Unset, data)

        sa2 = _parse_sa2(d.pop("sa2", UNSET))

        def _parse_sa3(data: object) -> NamedArea | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                sa3_type_0 = NamedArea.from_dict(data)

                return sa3_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NamedArea | None | Unset, data)

        sa3 = _parse_sa3(d.pop("sa3", UNSET))

        def _parse_sa4(data: object) -> NamedArea | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                sa4_type_0 = NamedArea.from_dict(data)

                return sa4_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NamedArea | None | Unset, data)

        sa4 = _parse_sa4(d.pop("sa4", UNSET))

        def _parse_gccsa(data: object) -> NamedArea | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                gccsa_type_0 = NamedArea.from_dict(data)

                return gccsa_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NamedArea | None | Unset, data)

        gccsa = _parse_gccsa(d.pop("gccsa", UNSET))

        def _parse_sa1(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sa1 = _parse_sa1(d.pop("sa1", UNSET))

        def _parse_ward(data: object) -> None | Unset | Ward:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                ward_type_0 = Ward.from_dict(data)

                return ward_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | Ward, data)

        ward = _parse_ward(d.pop("ward", UNSET))

        enriched_address_boundaries = cls(
            lga=lga,
            state_electorate=state_electorate,
            commonwealth_electorate=commonwealth_electorate,
            mesh_block=mesh_block,
            sa2=sa2,
            sa3=sa3,
            sa4=sa4,
            gccsa=gccsa,
            sa1=sa1,
            ward=ward,
        )

        enriched_address_boundaries.additional_properties = d
        return enriched_address_boundaries

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

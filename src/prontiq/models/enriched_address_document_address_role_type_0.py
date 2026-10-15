from typing import Literal

EnrichedAddressDocumentAddressRoleType0 = Literal["PRIMARY", "SECONDARY"]

ENRICHED_ADDRESS_DOCUMENT_ADDRESS_ROLE_TYPE_0_VALUES: set[
    EnrichedAddressDocumentAddressRoleType0
] = {
    "PRIMARY",
    "SECONDARY",
}


def check_enriched_address_document_address_role_type_0(
    value: str,
) -> EnrichedAddressDocumentAddressRoleType0:
    if value in ENRICHED_ADDRESS_DOCUMENT_ADDRESS_ROLE_TYPE_0_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ENRICHED_ADDRESS_DOCUMENT_ADDRESS_ROLE_TYPE_0_VALUES!r}"
    )

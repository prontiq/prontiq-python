from typing import Literal

ValidateAddressResponseProntiqMatchQuality = Literal["high", "low", "medium", "none"]

VALIDATE_ADDRESS_RESPONSE_PRONTIQ_MATCH_QUALITY_VALUES: set[
    ValidateAddressResponseProntiqMatchQuality
] = {
    "high",
    "low",
    "medium",
    "none",
}


def check_validate_address_response_prontiq_match_quality(
    value: str,
) -> ValidateAddressResponseProntiqMatchQuality:
    if value in VALIDATE_ADDRESS_RESPONSE_PRONTIQ_MATCH_QUALITY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {VALIDATE_ADDRESS_RESPONSE_PRONTIQ_MATCH_QUALITY_VALUES!r}"
    )

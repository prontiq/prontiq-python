from typing import Literal

AddressErrorCode = Literal[
    "INTERNAL_ERROR",
    "INVALID_API_KEY",
    "INVALID_PARAMETERS",
    "MISSING_API_KEY",
    "NOT_FOUND",
    "PRODUCT_NOT_ALLOWED",
    "QUOTA_EXCEEDED",
    "RATE_LIMITED",
]

ADDRESS_ERROR_CODE_VALUES: set[AddressErrorCode] = {
    "INTERNAL_ERROR",
    "INVALID_API_KEY",
    "INVALID_PARAMETERS",
    "MISSING_API_KEY",
    "NOT_FOUND",
    "PRODUCT_NOT_ALLOWED",
    "QUOTA_EXCEEDED",
    "RATE_LIMITED",
}


def check_address_error_code(value: str) -> AddressErrorCode:
    if value in ADDRESS_ERROR_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ADDRESS_ERROR_CODE_VALUES!r}"
    )

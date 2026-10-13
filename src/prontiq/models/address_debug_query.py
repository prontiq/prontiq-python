from typing import Literal

AddressDebugQuery = Literal["false", "true"]

ADDRESS_DEBUG_QUERY_VALUES: set[AddressDebugQuery] = {
    "false",
    "true",
}


def check_address_debug_query(value: str) -> AddressDebugQuery:
    if value in ADDRESS_DEBUG_QUERY_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {ADDRESS_DEBUG_QUERY_VALUES!r}"
    )

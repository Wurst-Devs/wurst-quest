from typing import Any
from .data_object import DataObject


def growth(
    level: int, growth_rate: float, factor: float, base: int, base_level: int
) -> int:
    return round(
        max(
            (pow(max(level, 0), growth_rate) - pow(base_level, growth_rate)) * factor
            + base,
            0,
        )
    )


def clone(obj: Any) -> Any:
    return DataObject.cloneAny(obj)

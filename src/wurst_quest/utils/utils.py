def growth(
    level: int, growth_rate: float, factor: float, base: int, base_level: int
) -> int:
    return int(
        max(
            (pow(max(level, 0), growth_rate) - pow(base_level, growth_rate)) * factor
            + base,
            0,
        )
    )

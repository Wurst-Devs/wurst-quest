from typing import List

from .entity import Entity


class MonsterEntity(Entity):
    def __init__(self, **kwargs) -> None:
        self.base_name: str = "unknown"
        self.experience_gain: int = 0
        self.attack: int = 0
        self.loot: List[str] = []
        super().__init__(**kwargs)

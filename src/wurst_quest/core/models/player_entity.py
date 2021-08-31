from typing import Dict, List, Tuple
from wurst_quest.core.enums import PlayerGear

from .entity import Entity
from .item import Item


class PlayerEntity(Entity):
    def __init__(self, **kwargs) -> None:
        self.race: str = "unknown"
        self.job: str = "unknown"
        self.experience: int = 0
        self.inventory: List[Item] = []
        self.equipped: Dict[PlayerGear, Item] = {PlayerGear.WEAPON: None}
        super().__init__(**kwargs)

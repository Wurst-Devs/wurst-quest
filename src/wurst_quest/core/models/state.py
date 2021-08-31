from enum import Enum
import random
from typing import Any
from wurst_quest.core.models.monster_entity import MonsterEntity

from wurst_quest.utils import DataObject
from wurst_quest.core import Location

from .player_entity import PlayerEntity


class State(DataObject):
    def __init__(self, **kwargs) -> None:
        self.status: str = "TODO"  # text to display
        self.duration: int = 3  # time to wait
        self.location: Location = Location.CITY
        self.player: PlayerEntity = PlayerEntity()  # TODO create in another place
        self.monster: MonsterEntity = None  # MonsterEntity

        self.seed: Any = None
        self.random: random.Random = None

        super().__init__(**kwargs)

        self.set_seed(random.random())

    def set_seed(self, seed) -> None:
        self.seed = seed
        self.random = random.Random(seed)

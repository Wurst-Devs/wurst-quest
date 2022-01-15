import random
from typing import Any

from wurst_quest.utils import DataObject
from wurst_quest.core import Location
from wurst_quest.core.models import MonsterEntity

from .player_entity import PlayerEntity


class State(DataObject):
    def __init__(self, **kwargs) -> None:
        self.status: str = "TODO"  # text to display
        self.duration: int = 0  # time to wait
        self.location: Location = Location.CITY
        self.player: PlayerEntity = None
        self.monster: MonsterEntity = None

        self.locked: bool = False

        self.seed: Any = None
        self.random: random.Random = None

        super().__init__(**kwargs)

        self.set_seed(random.random())

    def set_seed(self, seed) -> None:
        self.seed = seed
        self.random = random.Random(seed)

from enum import Enum
import random

from wurst_quest.utils import DataObject
from wurst_quest.core import Location

from .player_entity import PlayerEntity


class State(DataObject):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.status = "TODO"  # text to display
        self.duration = 3  # time to wait
        self.location = Location.CITY
        self.player = PlayerEntity()  # TODO create in another place
        self.monster = None  # MonsterEntity

        self.seed = None
        self.random = None

        self.set_seed(random.random())

    def set_seed(self, seed) -> None:
        self.seed = seed
        self.random = random.Random(seed)

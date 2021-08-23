from enum import Enum
import random

from utils import DataObject

from .player_entity import PlayerEntity
from .enums import Location


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

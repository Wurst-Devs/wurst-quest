from enum import Enum
from .player_entity import PlayerEntity
from .enums import Location


class State:
    def __init__(self) -> None:
        self.status = "TODO"  # text to display
        self.duration = 3  # time to wait
        self.location = Location.CITY
        self.player = PlayerEntity()  # TODO create in another place
        self.monster = None  # MonsterEntity

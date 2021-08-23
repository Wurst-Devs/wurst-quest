from enum import Enum


class ActionType(Enum):
    TODO = 1


class Location(Enum):
    CITY = 1
    OUTSIDE = 2
    BATTLE = 3


class PlayerGear(Enum):
    WEAPON = 1

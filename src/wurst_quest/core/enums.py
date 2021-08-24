from enum import Enum


class ActionType(Enum):
    TODO = 1


class Location(Enum):
    CITY = 1
    OUTSIDE = 2
    BATTLE = 3


class PlayerGear(Enum):
    WEAPON = 1


class Adjective(Enum):
    MONSTER = 1
    EQUIPMENT = 2
    LOOT = 3

from enum import Enum


class ActionType(Enum):
    WAIT = 0
    BUY = 1
    LEAVE = 2
    RETREAT = 3
    SEARCH = 4
    BATTLE = 5
    FLEE = 6


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

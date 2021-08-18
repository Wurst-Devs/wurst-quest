from .entity import Entity
from .enums import PlayerGear


class PlayerEntity(Entity):
    def __init__(self) -> None:
        super().__init__()
        self.race = "unkown"
        self.job = "unknown"
        self.experience = 0
        self.inventory = []
        self.equipped = {PlayerGear.WEAPON: None}

from wurst_quest.core.enums import PlayerGear

from .entity import Entity


class PlayerEntity(Entity):
    def __init__(self, **kwargs) -> None:
        self.race = "unknown"
        self.job = "unknown"
        self.experience = 0
        self.inventory = []
        self.equipped = {PlayerGear.WEAPON: None}
        super().__init__(**kwargs)

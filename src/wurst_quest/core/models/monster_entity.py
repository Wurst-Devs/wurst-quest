from .entity import Entity


class MonsterEntity(Entity):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.base_name = "unknown"
        self.experience_gain = 0
        self.attack = 0
        self.loot = []

from .entity import Entity


class MonsterEntity(Entity):
    def __init__(self) -> None:
        super().__init__()
        self.attack = 0
        self.loot = []

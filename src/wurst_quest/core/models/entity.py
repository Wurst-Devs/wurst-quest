from abc import ABCMeta

from wurst_quest.utils import DataObject


class Entity(DataObject, metaclass=ABCMeta):
    def __init__(self, **kwargs) -> None:
        self.name: str = "unknown"
        self.level: int = 0
        self.max_hp: int = 0
        self.hp: int = 0
        super().__init__(**kwargs)

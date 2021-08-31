from abc import ABCMeta

from wurst_quest.utils import DataObject


class Entity(DataObject, metaclass=ABCMeta):
    def __init__(self, **kwargs) -> None:
        self.name = "unknown"
        self.level = 0
        self.max_hp = 0
        self.hp = 0
        super().__init__(**kwargs)

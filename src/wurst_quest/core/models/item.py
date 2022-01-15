from wurst_quest.utils import DataObject


class Item(DataObject):
    def __init__(self, **kwargs) -> None:
        self.name: str = "unknown"
        self.value: int = 0
        super().__init__(**kwargs)

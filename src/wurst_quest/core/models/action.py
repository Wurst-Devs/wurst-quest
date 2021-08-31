from wurst_quest.utils import DataObject
from wurst_quest.core import ActionType


class Action(DataObject):
    def __init__(self, action_type: ActionType, **kwargs) -> None:
        self.type: ActionType = action_type
        super().__init__(**kwargs)

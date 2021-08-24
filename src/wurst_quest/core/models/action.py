from wurst_quest.utils import DataObject

from wurst_quest.core import ActionType


class Action(DataObject):
    def __init__(self, action_type: ActionType, **kwargs) -> None:
        super().__init__(**kwargs)
        self.type = action_type

from utils import DataObject

from .enums import ActionType


class Action(DataObject):
    def __init__(self, action_type: ActionType, **kwargs) -> None:
        super().__init__(**kwargs)
        self.type = action_type

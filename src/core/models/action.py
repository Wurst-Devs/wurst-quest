from enum import Enum


class ActionType(Enum):
    TODO = 1


class Action:
    def __init__(self, action_type: ActionType) -> None:
        self.type = action_type

from .enums import ActionType


class Action:
    def __init__(self, action_type: ActionType) -> None:
        self.type = action_type

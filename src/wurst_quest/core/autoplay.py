from .models import Action, State
from .enums import ActionType


class Autoplay:
    def __init__(self) -> None:
        pass

    def next_action(self, state: State) -> Action:
        return Action(ActionType.TODO)

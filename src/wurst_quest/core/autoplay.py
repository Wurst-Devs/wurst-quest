from wurst_quest.core.models import Action, ActionType, State


class Autoplay:
    def __init__(self) -> None:
        pass

    def next_action(self, state: State) -> Action:
        return Action(ActionType.TODO)

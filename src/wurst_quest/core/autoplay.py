from .models import Action, State
from .enums import ActionType, Location


class Autoplay:
    def __init__(self) -> None:
        pass

    def next_action(self, state: State) -> Action:
        if state.locked:
            return Action(ActionType.WAIT)
        elif state.location == Location.CITY:
            return Action(ActionType.LEAVE)
        elif state.location == Location.OUTSIDE:
            if state.player.hp < state.player.max_hp * 0.25:
                return Action(ActionType.RETREAT)
            else:
                return Action(ActionType.SEARCH)
        elif state.location == Location.BATTLE:
            if state.player.hp < state.player.max_hp * 0.25:
                return Action(ActionType.FLEE)
            else:
                return Action(ActionType.BATTLE)
        else:
            return Action(ActionType.WAIT)

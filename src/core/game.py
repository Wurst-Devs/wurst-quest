import logging

from .models import Action, State


class Game:
    def __init__(self) -> None:
        pass

    def init(self) -> None:
        logging.info("loading data...")
        # TODO

    def new_game(self) -> State:
        logging.info("new game:")
        return State()

    def compute(self, state: State, action: Action) -> State:
        new_state = State()

        # TODO

        return new_state
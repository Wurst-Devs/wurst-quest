import logging

from wurst_quest.core.models import Action, State

from .content import Content


class Game:
    def __init__(self) -> None:
        pass

    @property
    def content(self) -> Content:
        return Content.get_instance()

    def init(self) -> None:
        logging.info("loading data...")
        self.content.init()

        # TODO

    def new_game(self) -> State:
        logging.info("new game:")
        return State()

    def compute(self, state: State, action: Action) -> State:
        new_state = State()

        # TODO

        return new_state

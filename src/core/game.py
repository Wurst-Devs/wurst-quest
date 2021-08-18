import logging
import pandas as pd
import os

from .models import Action, State


class Content:
    def __init__(self):
        self.monsters = pd.read_csv(os.path.join("res", "monsters.csv"))
        self.equipments = pd.read_csv(os.path.join("res", "equipments.csv"))
        self.adjectives = pd.read_csv(os.path.join("res", "adjectives.csv"))


class Game:
    def __init__(self) -> None:
        self.content = None

    def init(self) -> None:
        logging.info("loading data...")
        self.content = Content()

        # TODO

    def new_game(self) -> State:
        logging.info("new game:")
        return State()

    def compute(self, state: State, action: Action) -> State:
        new_state = State()

        # TODO

        return new_state

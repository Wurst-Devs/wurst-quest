import logging
import pandas as pd
import os

from .models import Action, State


class Game:
    def __init__(self) -> None:
        self.monsters = None
        self.equipments = None

    def init(self) -> None:
        logging.info("loading data...")

        self.monsters = pd.read_csv(os.path.join("res", "monsters.csv"))
        self.equipments = pd.read_csv(os.path.join("res", "equipments.csv"))

        # TODO

    def new_game(self) -> State:
        logging.info("new game:")
        return State()

    def compute(self, state: State, action: Action) -> State:
        new_state = State()

        # TODO

        return new_state

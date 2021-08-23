import pandas as pd
import os

from utils import Singleton


class Content(Singleton):
    def __init__(self):
        super().__init__()
        self.monsters = None
        self.equipments = None
        self.adjectives = None

    def init(self):
        self.monsters = pd.read_csv(os.path.join("res", "monsters.csv")).to_dict(
            "records"
        )
        self.equipments = pd.read_csv(os.path.join("res", "equipments.csv")).to_dict(
            "records"
        )
        self.adjectives = pd.read_csv(os.path.join("res", "adjectives.csv")).to_dict(
            "records"
        )

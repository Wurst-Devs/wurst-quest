import pandas as pd
import os


class Content:
    def __init__(self):
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

import pandas as pd
import os
from typing import List, Dict

from wurst_quest.utils import Singleton


def read_csv(name, *, arrays=[]) -> List[dict]:
    df = pd.read_csv(os.path.join("res", f"{name}.csv"))

    for col_name in arrays:
        df[col_name] = df[col_name].apply(lambda d: d.split("|"))

    return df.to_dict("records")


class Content(Singleton):
    def __init__(self) -> None:
        super().__init__()
        self.monsters = None
        self.equipments = None
        self.adjectives = None

    def init(self) -> None:
        self.monsters = read_csv("monsters", arrays=["loot"])
        self.equipments = read_csv("equipments")
        self.adjectives = read_csv("adjectives", arrays=["monster", "equipment"])

    def get_adjectives(self, name: str) -> Dict[int, List[str]]:
        if name not in self.adjectives[0]:
            return {}

        adj = {row["bonus"]: row[name] for row in self.adjectives}
        adj[0] = [""]

        return adj

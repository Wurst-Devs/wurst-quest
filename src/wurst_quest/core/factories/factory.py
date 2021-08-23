from abc import ABC
from random import Random
from typing import Tuple, Callable, Optional, list, Union

from wurst_quest.core import Content
from wurst_quest.core.enums import Adjective


class Factory(ABC):
    def __init__(self, random: Random) -> None:
        super().__init__()
        self.random = random

    @property
    def content(self) -> Content:
        return Content.get_instance()

    def choice(self, population: list, weights: Optional[Union[Callable, list]] = None):
        if callable(weights):
            return self.random.choices(
                population, [weights(p) for p in population], k=1
            )[0]
        elif type(weights) is list:
            return self.random.choices(population, weights, k=1)[0]
        else:
            return self.random.choice(population)

    def get_bonus(self, adj_type: Adjective) -> Tuple[int, str]:
        adj = self.content.get_adjectives(adj_type)

        selected = self.choice(adj.keys(), lambda b: pow(2, -abs(b)))

        return selected, self.choice(adj[selected])

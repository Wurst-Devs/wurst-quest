from abc import ABC
from random import Random
from typing import Tuple, Callable, Optional, Union

from wurst_quest.core import Content, Adjective


class Factory(ABC):
    def __init__(self, random: Random) -> None:
        super().__init__()
        self.random = random

    @property
    def content(self) -> Content:
        return Content.get_instance()

    def _choice(
        self, population: list, weights: Optional[Union[Callable, list]] = None
    ):
        population = list(population)
        if callable(weights):
            weights = [weights(p) for p in population]
        if type(weights) is list:
            max_weight = max(weights)
            weights = [w / max_weight for w in weights]
            return self.random.choices(population, weights, k=1)[0]
        else:
            return self.random.choice(population)

    def _get_bonus(self, adj_type: Adjective) -> Tuple[int, str]:
        adj = self.content.get_adjectives(adj_type)

        selected = self._choice(adj.keys(), lambda b: pow(2, -abs(b)))

        return selected, self._choice(adj[selected])

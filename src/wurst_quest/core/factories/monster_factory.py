from typing import List, Tuple

from wurst_quest.core.models import MonsterEntity, Item
from wurst_quest.core import Adjective
from wurst_quest.utils import growth

from .factory import Factory


MONSTER_GROWTH = 2
MONSTER_XP_FACTOR = 1
MONSTER_HP_FACTOR = 0.5
MONSTER_ATTACK_FACTOR = 1 / 10  # 5 turns to kill exactly same


class MonsterFactory(Factory):
    def _available_monsters(self, min_level: int) -> Tuple[List[dict], List[int]]:
        return [
            monster
            for monster in self.content.monsters
            if monster["min_level"] >= min_level
        ]

    def generate_monster(self, min_level: int) -> MonsterEntity:
        monsters = self._available_monsters(min_level)
        monster_data = self._choice(monsters, lambda monster: monster["rarity"])

        bonus, adjective = self._get_bonus(Adjective.MONSTER)

        monster = MonsterEntity(
            name=f"{adjective} {monster_data['name']}".strip(),
            base_name=monster_data["name"],
            loot=monster_data["loot"],
            level=max(0, monster_data["min_level"] + bonus),
        )

        monster.update(
            experience_gain=growth(
                monster.level,
                MONSTER_GROWTH,
                MONSTER_XP_FACTOR,
                monster_data["xp"],
                monster_data["min_level"],
            ),
            max_hp=growth(
                monster.level,
                MONSTER_GROWTH,
                MONSTER_HP_FACTOR,
                monster_data["hp"],
                monster_data["min_level"],
            ),
            attack=growth(
                monster.level,
                MONSTER_GROWTH,
                MONSTER_ATTACK_FACTOR,
                monster_data["attack"],
                monster_data["min_level"],
            ),
        )

        monster.hp = monster.max_hp

        return monster

    def generate_loot(self, monster: MonsterEntity) -> Item:
        weights = [pow(2, -i) for i in range(len(monster.loot))]
        weights += [weights[-1]]  # chance for nothing is same as rarest item

        selected = self._choice(monster.loot + [None], weights)

        if selected is None:
            return None

        rarity = pow(2, monster.loot.index(selected))

        bonus, adjective = self._get_bonus(Adjective.LOOT)

        score = max(monster.level + rarity + bonus, 0)

        return Item(
            name=f"{adjective} {monster.base_name}'s {selected}".strip(), value=score
        )

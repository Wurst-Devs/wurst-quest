from wurst_quest.core import PlayerGear
from wurst_quest.core.models import PlayerEntity, Item
from wurst_quest.utils import growth

from .factory import Factory

PLAYER_GROWTH = 2
PLAYER_XP_FACTOR = 1
PLAYER_XP_BASE = 10
PLAYER_HP_FACTOR = 0.5
PLAYER_HP_BASE = 10
PLAYER_ATTACK_FACTOR = 1 / 10
PLAYER_ATTACK_BASE = 3


class PlayerFactory(Factory):
    def new_player(self) -> PlayerEntity:
        player = PlayerEntity(name="Player", level=0)

        return self.level_up(player)

    def level_up(self, player: PlayerEntity) -> PlayerEntity:
        player = player.clone()
        player.level += 1
        max_hp = growth(player.level, PLAYER_GROWTH, PLAYER_HP_FACTOR, PLAYER_HP_BASE)
        attack = growth(
            player.level, PLAYER_GROWTH, PLAYER_ATTACK_FACTOR, PLAYER_ATTACK_BASE
        )

        player.update(max_hp=max_hp, hp=max_hp)
        player.equipped[PlayerGear.WEAPON] = Item(name="Bare Hands", value=attack)
        return player

    def can_level_up(self, player: PlayerEntity) -> bool:
        return player.experience > growth(
            player.level, PLAYER_GROWTH, PLAYER_XP_FACTOR, PLAYER_XP_BASE
        )

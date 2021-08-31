from random import Random

from wurst_quest.core import Content, PlayerGear
from wurst_quest.core.models import PlayerEntity
from wurst_quest.core.factories import PlayerFactory

from tests.utils import TestResTestCase


class TestPlayerFactory(TestResTestCase):
    def setUp(self):
        Content.get_instance().init()

    def test_new_player(self):
        factory = PlayerFactory(Random(0))
        player = factory.new_player()
        self.assertEqual("Player", player.name)
        self.assertEqual(1, player.level)
        self.assertEqual(0, player.experience)
        self.assertEqual(10, player.max_hp)
        self.assertEqual(10, player.hp)
        self.assertIsNotNone(player.equipped[PlayerGear.WEAPON])
        self.assertEqual("Bare Hands", player.equipped[PlayerGear.WEAPON].name)
        self.assertEqual(3, player.equipped[PlayerGear.WEAPON].value)

    def test_can_level_up(self):
        factory = PlayerFactory(Random(0))
        self.assertFalse(factory.can_level_up(PlayerEntity(level=1, experience=10)))
        self.assertTrue(factory.can_level_up(PlayerEntity(level=1, experience=19)))

    def test_level_up(self):
        factory = PlayerFactory(Random(0))
        player = factory.level_up(
            PlayerEntity(level=3, max_hp=14, hp=13, experience=37)
        )
        self.assertEqual(4, player.level)
        self.assertEqual(0, player.experience)
        self.assertEqual(18, player.max_hp)
        self.assertEqual(18, player.hp)
        self.assertIsNotNone(player.equipped[PlayerGear.WEAPON])
        self.assertEqual("Bare Hands", player.equipped[PlayerGear.WEAPON].name)
        self.assertEqual(4, player.equipped[PlayerGear.WEAPON].value)

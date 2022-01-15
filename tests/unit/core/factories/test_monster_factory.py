from random import Random

from wurst_quest.core import Content
from wurst_quest.core.factories import MonsterFactory

from tests.utils import TestResTestCase


class TestMonsterFactory(TestResTestCase):
    def setUp(self):
        Content.get_instance().init()

    def test_generate_monster(self):
        factory = MonsterFactory(Random(3))
        monster = factory.generate_monster(3)
        self.assertEqual("f test_monster", monster.name)
        self.assertEqual("test_monster", monster.base_name)
        self.assertEqual(["test_1", "test_2"], monster.loot)
        self.assertEqual(5, monster.level)
        self.assertEqual(46, monster.experience_gain)
        self.assertEqual(18, monster.max_hp)
        self.assertEqual(5, monster.attack)
        self.assertEqual(monster.max_hp, monster.hp)

    def test_generate_loot(self):
        factory = MonsterFactory(Random(19))
        monster = factory.generate_monster(3)

        loot = factory.generate_loot(monster)
        self.assertEqual("a test_monster's test_2", loot.name)
        self.assertEqual(6, loot.value)

    def test_generate_loot_empty(self):
        factory = MonsterFactory(Random(5))
        monster = factory.generate_monster(3)

        loot = factory.generate_loot(monster)
        self.assertIsNone(loot)

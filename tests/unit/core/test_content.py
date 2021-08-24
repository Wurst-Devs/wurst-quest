from wurst_quest.core import Content, Adjective

from tests.utils import TestResTestCase


class TestContent(TestResTestCase):
    def setUp(self):
        Content._Singleton__instance = None

    def test_get_adjectives(self):
        content = Content()
        content.init()
        self.assertIsNotNone(content.adjectives)
        adj = content.get_adjectives(Adjective.MONSTER)
        expected = {-3: ["a"], -2: ["b"], -1: ["c"], 1: ["d", "e"], 2: ["f"], 0: [""]}
        self.assertDictDeepEqual(expected, adj)

    def test_monster(self):
        content = Content()
        content.init()
        self.assertIsNotNone(content.monsters)
        self.assertEqual(len(content.monsters), 1)
        expected = {
            "name": "test_monster",
            "rarity": 3,
            "xp": 30,
            "hp": 10,
            "attack": 3,
            "loot": ["test_1", "test_2"],
            "min_level": 3,
        }
        self.assertDictDeepEqual(expected, content.monsters[0])

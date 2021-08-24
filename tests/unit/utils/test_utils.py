from wurst_quest.utils.utils import growth
from tests.utils import CustomTestCase


class TestUtils(CustomTestCase):
    def test_growth(self):
        self.assertEqual(25, growth(2, 2, 1, 30, 3))
        self.assertEqual(30, growth(3, 2, 1, 30, 3))
        self.assertEqual(37, growth(4, 2, 1, 30, 3))

from wurst_quest.utils.utils import growth, clone
from tests.utils import CustomTestCase


class TestUtils(CustomTestCase):
    def test_growth(self):
        self.assertEqual(25, growth(2, 2, 1, 30, 3))
        self.assertEqual(30, growth(3, 2, 1, 30, 3))
        self.assertEqual(37, growth(4, 2, 1, 30, 3))


class TestUtilsClone(CustomTestCase):
    def test_clone_base(self):
        a = 1
        a, b = 2, clone(a)
        self.assertEqual(1, b)
        self.assertEqual(2, a)

        a = "test"
        a, b = "test2", clone(a)
        self.assertEqual("test", b)
        self.assertEqual("test2", a)

    def test_clone_list(self):
        a = [3, 2, 1]
        b = clone(a)
        a.sort()
        self.assertEqual([3, 2, 1], b)
        self.assertEqual([1, 2, 3], a)

    def test_clone_dict(self):
        a = {"a": 1, "b": 2}
        b = clone(a)
        a["a"] = 3
        self.assertEqual(1, b["a"])
        self.assertEqual(3, a["a"])

    def test_clone_set(self):
        a = {"a", "b"}
        b = clone(a)
        a.remove("a")
        self.assertEqual({"a", "b"}, b)
        self.assertEqual({"b"}, a)

from unittest import TestCase
from _pytest.monkeypatch import MonkeyPatch
import os.path


class CustomTestCase(TestCase):
    def assertDictDeepEqual(self, first: dict, second: dict) -> None:
        self.assertListEqual(list(first.keys()), list(second.keys()))
        for key in first:
            self.assertEqual(type(first[key]), type(second[key]))
            if type(first[key]) == dict:
                self.assertDictDeepEqual(first[key], second[key])
            elif type(first[key]) == list:
                self.assertListDeepEqual(first[key], second[key])
            else:
                self.assertEqual(first[key], second[key])

    def assertListDeepEqual(self, first: list, second: list) -> None:
        self.assertCountEqual(first, second)
        for index in range(len(first)):
            self.assertEqual(type(first[index]), type(second[index]))
            if type(first[index]) == dict:
                self.assertDictDeepEqual(first[index], second[index])
            elif type(first[index]) == list:
                self.assertListDeepEqual(first[index], second[index])
            else:
                self.assertEqual(first[index], second[index])


class TestResTestCase(CustomTestCase):
    @classmethod
    def setUpClass(cls):
        cls.original_join = os.path.join

        def mock_join(*args):
            return cls.original_join("tests", *args)

        MonkeyPatch().setattr(os.path, "join", mock_join)

    @classmethod
    def tearDownClass(cls):
        MonkeyPatch().setattr(os.path, "join", cls.original_join)

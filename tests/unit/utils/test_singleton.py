from wurst_quest.utils import Singleton
from wurst_quest.utils.singleton import SingletonError


from tests.utils import CustomTestCase


class MySingleton(Singleton):
    pass


class MyOtherSingleton(Singleton):
    pass


class TestSingleton(CustomTestCase):
    def setUp(self):
        MySingleton._Singleton__instance = None
        MyOtherSingleton._Singleton__instance = None

    def test_get_instance_only(self):
        self.assertIsNone(MySingleton._Singleton__instance)
        instance = MySingleton.get_instance()
        self.assertEqual(instance, MySingleton._Singleton__instance)
        self.assertEqual(instance, MySingleton.get_instance())

    def test_get_instance_init(self):
        self.assertIsNone(MySingleton._Singleton__instance)
        instance = MySingleton()
        self.assertEqual(instance, MySingleton._Singleton__instance)
        self.assertEqual(instance, MySingleton.get_instance())

    def test_get_instance_init_2_classes(self):
        self.assertIsNone(MySingleton._Singleton__instance)
        self.assertIsNone(MyOtherSingleton._Singleton__instance)
        instance = MySingleton()
        other_instance = MyOtherSingleton()
        self.assertEqual(instance, MySingleton._Singleton__instance)
        self.assertEqual(other_instance, MyOtherSingleton._Singleton__instance)
        self.assertNotEqual(instance, other_instance)
        self.assertEqual(instance, MySingleton.get_instance())
        self.assertEqual(other_instance, MyOtherSingleton.get_instance())

    def test_cannot_init_twice(self):
        self.assertIsNone(MySingleton._Singleton__instance)
        instance = MySingleton()
        other_instance = None
        try:
            other_instance = MySingleton()
            self.fail()
        except SingletonError as e:
            self.assertEqual(
                e.args,
                ("MySingleton was already created, use MySingleton.get_instance()",),
            )
        self.assertIsNone(other_instance)
        self.assertEqual(instance, MySingleton._Singleton__instance)
        self.assertEqual(instance, MySingleton.get_instance())

    def test_cannot_init_after_get_instance(self):
        self.assertIsNone(MySingleton._Singleton__instance)
        instance = MySingleton.get_instance()
        other_instance = None
        try:
            other_instance = MySingleton()
            self.fail()
        except SingletonError as e:
            self.assertEqual(
                e.args,
                ("MySingleton was already created, use MySingleton.get_instance()",),
            )
        self.assertIsNone(other_instance)
        self.assertEqual(instance, MySingleton._Singleton__instance)
        self.assertEqual(instance, MySingleton.get_instance())

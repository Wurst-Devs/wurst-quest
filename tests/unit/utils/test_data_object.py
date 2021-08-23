from src.utils import DataObject

from tests.utils import CustomTestCase


class MyDataObject(DataObject):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.myattr = "a"


class TestDataObject(CustomTestCase):
    def test_init(self):
        obj = MyDataObject(name="test", myattr="b", list=[1, 2, 3])
        self.assertEqual("test", obj.name)
        self.assertEqual("a", obj.myattr)
        self.assertListEqual([1, 2, 3], obj.list)

    def test_update(self):
        obj = MyDataObject()
        self.assertEqual("a", obj.myattr)
        try:
            u = obj.name
            self.fail()
        except AttributeError:
            pass
        obj.update(name="test", myattr="b")
        self.assertEqual("test", obj.name)
        self.assertEqual("b", obj.myattr)

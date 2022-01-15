from wurst_quest.utils import DataObject

from tests.utils import CustomTestCase


class MyDataObject(DataObject):
    def __init__(self, **kwargs) -> None:
        self.myattr = "a"
        self.name = "test"
        self.list = [1, 2, 3]
        self.sub = None
        super().__init__(**kwargs)


class TestDataObject(CustomTestCase):
    def test_init(self):
        obj = MyDataObject(name="test2", myattr="b", list=[4, 5, 6])
        self.assertEqual("test2", obj.name)
        self.assertEqual("b", obj.myattr)
        self.assertListEqual([4, 5, 6], obj.list)

    def test_update(self):
        obj = MyDataObject()
        self.assertEqual("a", obj.myattr)
        self.assertEqual("test", obj.name)
        obj.update(name="test2", myattr="b")
        self.assertEqual("b", obj.myattr)
        self.assertEqual("test2", obj.name)

    def test_clone(self):
        obj = MyDataObject()
        obj2 = obj.clone()
        obj.myattr = "b"
        self.assertEqual("b", obj.myattr)
        self.assertEqual("a", obj2.myattr)

    def test_clone_with_attributes(self):
        obj = MyDataObject()
        obj2 = obj.clone(myattr="c")
        obj.myattr = "b"
        self.assertEqual("b", obj.myattr)
        self.assertEqual("c", obj2.myattr)

    def test_clone_subdata(self):
        obj = MyDataObject(sub=MyDataObject())
        obj2 = obj.clone()
        obj.sub.myattr = "b"
        self.assertEqual("b", obj.sub.myattr)
        self.assertEqual("a", obj2.sub.myattr)

    def test_clone_sublist(self):
        obj = MyDataObject(list=[6, 5, 4])
        obj2 = obj.clone()
        obj.list.sort()
        self.assertEqual([4, 5, 6], obj.list)
        self.assertEqual([6, 5, 4], obj2.list)

    def test_repr(self):
        obj = MyDataObject(name="test", sub=MyDataObject())
        self.assertEqual(
            "MyDataObject{myattr: a, name: test, list: [1, 2, 3], sub: MyDataObject{myattr: a, name: test, list: [1, 2, 3], sub: None}}",
            str(obj),
        )

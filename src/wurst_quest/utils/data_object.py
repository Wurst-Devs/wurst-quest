from abc import ABC
from typing import Any


class DataObject(ABC):
    def __init__(self, **kwargs) -> None:
        super().__init__()
        self.update(**kwargs)

    def update(self, **kwargs) -> None:
        for key in kwargs:
            setattr(self, key, kwargs[key])

    def clone(self, **kwargs) -> Any:
        data = self.__dict__.copy()
        for attribute in data:
            data[attribute] = DataObject.cloneAny(data[attribute])
        clone = self.__class__(**data)
        clone.update(**kwargs)
        return clone

    @classmethod
    def cloneAny(cls, obj: Any) -> Any:
        if issubclass(type(obj), DataObject):
            return obj.clone()
        elif type(obj) is dict:
            return {key: DataObject.cloneAny(obj[key]) for key in obj}
        elif type(obj) is list:
            return [DataObject.cloneAny(value) for value in obj]
        elif type(obj) is set:
            return {DataObject.cloneAny(value) for value in obj}
        else:
            return obj

    def __repr__(self) -> str:
        data = self.__dict__
        data_repr = ", ".join(f"{attribute}: {data[attribute]}" for attribute in data)
        return f"{self.__class__.__name__}{{{data_repr}}}"

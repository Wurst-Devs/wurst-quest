from abc import ABC


class DataObject(ABC):
    def __init__(self, **kwargs) -> None:
        super().__init__()
        self.update(**kwargs)

    def update(self, **kwargs) -> None:
        for key in kwargs:
            setattr(self, key, kwargs[key])

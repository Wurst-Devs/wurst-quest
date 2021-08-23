from abc import ABC


class SingletonError(Exception):
    pass


class Singleton(ABC):
    __instance = None

    def __init__(self) -> None:
        super().__init__()
        if self.__class__.__instance is not None:
            raise SingletonError(
                f"{self.__class__.__name__} was already created, use {self.__class__.__name__}.get_instance()"
            )
        self.__class__.__instance = self

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

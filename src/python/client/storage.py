import abc


class Storage(abc.ABC):
    @abc.abstractmethod
    def add(self, value: dict[str, str]) -> None:
        pass

    def get_history(self) -> list[dict[str, str]]:
        """
        Returns the history of stored values.
        :return: List of stored values.
        """
        return getattr(self, "history", [])


class InMemoryStorage(Storage):
    """
    A simple in-memory storage class that can be used to store key-value pairs.
    """

    def __init__(self):
        self.history = []

    def add(self, value: dict[str, str]) -> None:
        self.history.append(value)

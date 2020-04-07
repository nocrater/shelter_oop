from abc import ABC, abstractmethod


class Position(ABC):
    @abstractmethod
    def do_work(self, employee):
        pass

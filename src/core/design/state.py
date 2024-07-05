from abc import ABC, abstractmethod

class IState(ABC):
    @abstractmethod
    def evaluate(self, input):
        pass
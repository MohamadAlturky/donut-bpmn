from abc import ABC, abstractmethod

class BaseTask(ABC):
    @abstractmethod
    def handle(self, input):
        pass        
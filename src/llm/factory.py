from abc import ABC, abstractmethod

class LLMFactory(ABC):
    
    @abstractmethod
    def create(self):
        pass        
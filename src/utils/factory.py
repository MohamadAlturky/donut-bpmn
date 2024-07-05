from abc import ABC, abstractmethod

class LLMFactory(ABC):
    
    @abstractmethod
    def create(self, model_name : str = None):
        pass        
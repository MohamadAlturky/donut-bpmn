from core.design.state import IState

class InitialState(IState):
    
    def __init__(self, task):
        self.task = task
        
    def evaluate(self, input):
        try:
            generated = self.task.executor.kickoff(input)
        except:
            self.task.state = self.task.GENERATING_ERROR_STATE
            return None

        try:
            result = self.task.mapper.map(generated)
            self.task.state = self.task.COMPLETED_STATE
            return result
        except:
            self.task.MAPPING_ERROR_STATE.generated_result = generated
            self.task.state = self.task.MAPPING_ERROR_STATE
            return None

class MappingErrorState(IState):
    
    def __init__(self, task):
        self.task = task
        self.error_count = 0
        self.generated_result = None
        
    def evaluate(self, input):
        self.error_count = self.error_count + 1

        if self.error_count > self.task.mapping_error_tolerance:
            self.error_count = 0
            self.task.state = self.task.GENERATING_ERROR_STATE
            return None

        try:
            result = self.task.mapper.map(self.generated_result)
            self.task.state = self.task.COMPLETED_STATE
            return result
        except:
            self.task.state = self.task.MAPPING_ERROR_STATE
            return None



class GeneratingErrorState(IState):
    
    def __init__(self, task):
        self.task = task
        self.error_count = 0
        
    def evaluate(self, input):
        self.error_count = self.error_count + 1

        if self.error_count > self.task.generating_error_tolerance:
            self.task.state = self.task.FAILURE_STATE
            return None

        try:
            generated = self.task.executor.kickoff(input)
        except:
            self.task.state = self.task.GENERATING_ERROR_STATE
            return None

        try:
            result = self.task.mapper.map(generated)
            self.task.state = self.task.COMPLETED_STATE
            return result
        except:
            self.task.state = self.task.MAPPING_ERROR_STATE
            return None


"""
    the generation failed.
"""
class FailureState(IState):
    
    def __init__(self, task):
        self.task = task
        
    def evaluate(self, input):
        pass


"""
    the generation completed successfully.
"""
class CompletedState(IState):
    
    def __init__(self, task):
        self.task = task
        
    def evaluate(self, input):
        pass

from core.design.config import TaskConfig
from core.design.state import IState
from core.design.states import CompletedState, FailureState, GeneratingErrorState, InitialState, MappingErrorState
from core.spec.json.task_reader import load_task_specification
from crewai import Agent, Task, Crew

from mapping.model.config import MapperConfig
from mapping.mapper import Mapper

class LLMTask:
    def __init__(self, task_config:TaskConfig, mapper_config:MapperConfig):
        self.task_config = task_config
        self.mapper_config = mapper_config
        self.llm_factory = task_config.llm_factory 
        self.executor = None
        self.mapper = None
        self.INITIAL_STATE           :IState = InitialState(task=self)
        self.COMPLETED_STATE         :IState = CompletedState(task=self)
        self.MAPPING_ERROR_STATE     :IState = MappingErrorState(task=self)
        self.FAILURE_STATE           :IState = FailureState(task=self)
        self.GENERATING_ERROR_STATE  :IState = GeneratingErrorState(task=self)
        self.state                   :IState = self.INITIAL_STATE
        self.generating_error_tolerance = task_config.generating_error_tolerance
        self.mapping_error_tolerance = task_config.mapping_error_tolerance



    def __prepare(self):
        specification = load_task_specification(self.task_config.tasks_folder_path + self.task_config.task_name)
        agent = Agent(
            role=specification.role,
            goal=specification.goal,
            backstory=specification.backstory,
            allow_delegation=False,
            verbose=True,
            llm = self.llm_factory.create(self.task_config.model_name)
        )
        task = Task(
            description=specification.description,
            expected_output=specification.expected_output,
            output_json=self.task_config.output_type,
            agent=agent,
        )
        
        self.executor =Crew(
            agents=[agent],
            tasks=[task],
            verbose=2
        )
        self.mapper = Mapper(config=self.mapper_config)


    def evaluate(self, inputs):
        result = None
        error = "Err"
        while True:
            # create new connections to the llms.
            self.__prepare()
            print("\n\nstate\n\n")
            print(self.state)
            print("\n\nstate\n\n")
            
            result = self.state.evaluate(inputs)
            if self.state == self.COMPLETED_STATE:
                return result
            
            if self.state == self.FAILURE_STATE:
                return error
        
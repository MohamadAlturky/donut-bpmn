from crewai import Agent, Task, Crew
from mapping.model.obj import Obj
from mapping.model.config import MapperConfig
class Mapper():
    def __init__(self, config:MapperConfig):
        
        self.schema_descriptor = config.schema_descriptor
        self.mapping_type = config.binding_type
        
        if config.model_name is None:
            llm = config.llm_factory.create("codegemma")
        else:
            llm = config.llm_factory.create(config.model_name)
            
        mapper = Agent(
            role="json formating expert",
            goal="Your objective is to extract a json object from the provided text {text}",
            backstory="You're working to convert text containing data to json format with this format {json_descriptor}",
            allow_delegation=False,
            verbose=True,
            llm = llm
        )

        mapping = Task(
            description=(
                "\n"
                "1. Extract the data from the {text} and represent it in this format {json_descriptor}.\n"
            ),
            expected_output=(
                "json format representing the text."
            ),
            output_json=config.binding_type,
            agent=mapper,
        )
        self.crew = Crew(
            agents=[mapper],
            tasks=[mapping],
            verbose=2
        )

    def map(self, response):
        res = self.crew.kickoff(inputs={"text":response,"json_descriptor":self.schema_descriptor})
        print("-----------------------------")
        print("-----------------------------")
        print(res)
        print("-----------------------------")
        print("-----------------------------")
        obj = Obj(res)
        return obj
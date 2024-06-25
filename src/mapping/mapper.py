import json
from crewai import Agent, Task, Crew
from typing import TypeVar
from llm.ollama_factory import OllamaFactory

class Mapper():
    def __init__(self,binding_type:TypeVar):
        ollamaFactory = OllamaFactory()
        codegemma = ollamaFactory.create("codegemma")
        mapper = Agent(
            role="json formating expert",
            goal="Your objective is to extract a json object from the provided text {text}",
            backstory="You're working to convert text containing data to json format with this format {json_descriptor}",
            allow_delegation=False,
            verbose=True,
            llm = codegemma
        )

        mapping = Task(
            description=(
                "\n"
                "1. Extract the data from the {text} and represent it in this format {json_descriptor}.\n"
            ),
            expected_output=(
                "json format representing the text."
            ),
            output_json=binding_type,
            agent=mapper,
        )
        self.crew = Crew(
            agents=[mapper],
            tasks=[mapping],
            verbose=2
        )
        self.mapping_type = binding_type

    def map(self, response, schema_descriptor):
        res = self.crew.kickoff(inputs={"text":response,"json_descriptor":schema_descriptor})
        result : self.mapping_type = json.loads(res, object_hook=lambda d: self.mapping_type(**d))
        return result
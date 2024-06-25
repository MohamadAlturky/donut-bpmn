from crewai import Agent, Task, Crew
from pydantic import BaseModel

from tasks.base_task import BaseTask

class ActivityList(BaseModel):
    activities: list[str]

class ActivitySentences(BaseModel):
    sentence: str


class ActivityExtraction(BaseTask):
    def __init__(self,llm):
        
        extractor = Agent(
            role="business process modeling expert",
            goal="Your objective is to identify and list all the distinct activities mentioned in the business process description {process_description}",
            backstory="You're working on this proccess description to collect activities that helps your team to generate bpmn digrams",
            allow_delegation=False,
            verbose=True,
            llm = llm
        )

        extraction = Task(
            description=(
                "\n"
                "1. Extract all activities in the process description.\n"
                "2. Don't miss any of the activites.\n"
                "3. Don't mention any activity twice.\n"
                "4. Make the activity name short and concise.\n"
            ),
            expected_output=(
                "list of extracted activities from the process description,"
                "give me the list with json format."
            ),
            output_json=ActivityList,
            output_file="activities.json",  
            agent=extractor,
        )
        self.crew = Crew(
            agents=[extractor],
            tasks=[extraction],
            verbose=2
        )

    def handle(self, inputs):
        return self.crew.kickoff(inputs=inputs)







class ActivityExtractionMarker(BaseTask):
    def __init__(self,llm):
        
        marker = Agent(
            role="business process modeling expert",
            goal="Your objective is to identify the place where the activity {activity} mentioned in the business process description {process_description}",
            backstory="You're working on this proccess description to collect the places where the activity {activity} appeared",
            allow_delegation=False,
            verbose=True,
            llm = llm
        )

        marking = Task(
            description=(
                "\n"
                "1. Extract the sentence where the activity in the process description appeared.\n"
                "2. return the same sentence from the process description don't edit it.\n"
                "3. if the activity doesn't directly mentioned in the process description return not found directly.\n"
            ),
            expected_output=(
                "the sentences where the activity appeared"
            ),
            output_json=ActivitySentences,
            agent=marker,
        )
        self.crew = Crew(
            agents=[marker],
            tasks=[marking],
            verbose=2
        )

    def handle(self, inputs):
        return self.crew.kickoff(inputs=inputs)
















# class ActivityExtraction(BaseTask):
#     def __init__(self,llm):
        
#         extractor = Agent(
#             role="proccess modeling expert",
#             goal="Your objective is to identify and list all the distinct activities mentioned in the business process description {process_description}",
#             backstory="You're working on this proccess description to collect activities that helps your team to generate bpmn digrams",
#             allow_delegation=False,
#             verbose=True,
#             llm = llm
#         )

#         extraction = Task(
#             description=(
#                 "\n"
#                 "1. Extract all activities in the process description.\n"
#                 "2. Don't miss any of the activites.\n"
#                 "3. Don't mention any activity twice.\n"
#                 "4. Make the activity name short and concise.\n"
#                 "5. mark the place in the process description where the activity appeared for example <1>the activity in the process decription</1> for the first activity.\n"
#             ),
#             expected_output=(
#                 "list of extracted activities from the process description,"
#                 "give me the list with json format,"
#                 "and the edited process description in the formate of the step 5 in the task description."
#             ),
#             output_json=ActivityList,
#             output_file="activities.json",  
#             agent=extractor,
#         )
#         self.crew = Crew(
#             agents=[extractor],
#             tasks=[extraction],
#             verbose=2
#         )

#     def handle(self, inputs):
#         self.crew.kickoff(inputs=inputs)

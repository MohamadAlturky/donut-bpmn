from crewai import Agent, Task, Crew
from pydantic import BaseModel

from tasks.base_task import BaseTask


class NextActivity(BaseModel):
    activity: str
    condition: str

class ActivityRelationShipsList(BaseModel):
    next_activities: list[NextActivity]



class ActivityRelationShipsExtraction(BaseTask):
    def __init__(self,llm):
        
        extractor = Agent(
            role="business process modeling expert",
            goal="Your objective is to identify and list all the distinct activities mentioned in the business process description : {process_description} that are subsequent to the activity : {activity} and detect the conditions that leads to that activity",
            backstory="You're working on this proccess description to collect the relationships between activities to help your team to generate bpmn digrams",
            allow_delegation=False,
            verbose=True,
            llm = llm
        )

        extraction = Task(
            description=(
                "\n"
                "1. Extract all activities in the process description that are subsequent to the activity : {activity}.\n"
                "2. Don't miss any of the subsequent activites.\n"
                "3. Don't mention any activity twice.\n"
                "4. Make sure to specify activities just from this list {activities}.\n"
                "5. Make sure to specify the condition for the transition between these activities if there is no condition set it to null.\n"
            ),
            expected_output=(
                "list of extracted activities from the process description that are subsequent to the activity and the condition for the transition between these activities,"
                "give me the list with json format."
            ),
            output_json=ActivityRelationShipsList,
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

from pydantic import BaseModel


class Activity(BaseModel):
    name:str
    pool:str
    swimlane:str

class Activities(BaseModel):
    activities: list[Activity]

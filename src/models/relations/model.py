from pydantic import BaseModel

class NextActivity(BaseModel):
    activity: str
    condition: str

class ActivityRelationShipsList(BaseModel):
    next_activities: list[NextActivity]

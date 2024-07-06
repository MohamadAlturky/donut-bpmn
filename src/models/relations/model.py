from pydantic import BaseModel

class NextActivity(BaseModel):
    name: str
    condition: str

class ActivityRelationShipsList(BaseModel):
    next_activities: list[NextActivity]

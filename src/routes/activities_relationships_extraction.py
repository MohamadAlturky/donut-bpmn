from fastapi import APIRouter
from pydantic import BaseModel
from models.activities.model import Activities
from services.tasks import create_activities_relationships_extraction_task as task_creator
router = APIRouter(
    prefix="/activities_relationships"
)

class ExtractActivitiesRelationshipsRequest(BaseModel):
    process_description: str 
    activities_list: Activities

@router.post("/extract")
def extract_activities_from_pools_and_swimlanes(request:ExtractActivitiesRelationshipsRequest):
    result_list = []
    activities = [activity.name for activity in request.activities_list.activities]
    for activity in request.activities_list.activities:
        # print(f"**** {activity.name}")
        result = task_creator().evaluate(inputs={
            "process_description":request.process_description,
            "activity":activity.name,
            "activities":activities
        })
        result_list.append(result)
    return result_list
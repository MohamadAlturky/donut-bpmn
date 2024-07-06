from fastapi import APIRouter
from pydantic import BaseModel
from models.activities.model import Activity,Activities
from services.tasks import create_activities_relationships_extraction_task as task_creator
router = APIRouter(
    prefix="/activities_relationships"
)

class ExtractActivitiesRelationshipsRequest(BaseModel):
    process_description: str 
    activity: Activity
    activities_list:Activities

@router.post("/extract")
def extract_activities_from_pools_and_swimlanes(request:ExtractActivitiesRelationshipsRequest):
    result_list = []
    activities = [activity.name for activity in request.activities_list.activities]
    result = task_creator().evaluate(inputs={
        "process_description":request.process_description,
        "activity":request.activity,
        "activities":activities
    })
    result_list.append(result)
    return result_list

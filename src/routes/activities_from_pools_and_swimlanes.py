from fastapi import APIRouter
from pydantic import BaseModel
from models.pools_and_swimlanes.model import Pools
from services.tasks import create_activities_from_pools_and_swimlanes_extraction_task as task_creator
router = APIRouter(
    prefix="/activities"
)

class ExtractActivitiesFromPoolsAndSwimlanesRequest(BaseModel):
    process_description: str 
    pools_and_swimlanes: Pools

@router.post("/extract_from_pools_and_swimlanes")
def extract_activities_from_pools_and_swimlanes(request:ExtractActivitiesFromPoolsAndSwimlanesRequest):
    result = task_creator().evaluate(inputs={
        "process_description":request.process_description,
        "pools_and_swimlanes":request.pools_and_swimlanes
    })
    return result
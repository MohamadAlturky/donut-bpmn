from fastapi import APIRouter
from pydantic import BaseModel
from services.tasks import create_pools_and_swimlanes_extraction_task as task_creator
router = APIRouter(
    prefix="/pools_and_swimlanes"
)

class ExtractPoolsAndSwimlanesRequest(BaseModel):
    process_description: str 

@router.post("/extract")
def extract_pools_and_swimlanes(request:ExtractPoolsAndSwimlanesRequest):
    result = task_creator().evaluate(inputs={
        "process_description":request.process_description
    })
    return result
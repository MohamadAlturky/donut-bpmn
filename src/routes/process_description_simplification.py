from fastapi import APIRouter
from pydantic import BaseModel
from services.tasks import create_process_description_simplification_extraction_task as task_creator
router = APIRouter(
    prefix="/process_description"
)

class SimplifyProcessDescriptionRequest(BaseModel):
    process_description: str 

@router.post("/simplify")
def simplify_process_description(request:SimplifyProcessDescriptionRequest):
    result = task_creator().evaluate(inputs={
        "process_description":request.process_description
    })
    return result
import os
from models.activities.model import Activities
from models.pools_and_swimlanes.model import Pools
from core.design.task import LLMTask
from core.design.config import TaskConfig
from mapping.model.config import MapperConfig
from models.process_description.model import ProcessDescription
from models.relations.model import ActivityRelationShipsList
from utils.ollama_factory import OllamaFactory
from dotenv import load_dotenv
from settings import env


load_dotenv(override=True)
tasks_folder_path = os.getenv(env.TASKS_FOLDER_PATH)

def create_pools_and_swimlanes_extraction_task():        
    pools_and_swimlanes_task_config = TaskConfig(llm_factory=OllamaFactory(),
                                tasks_folder_path=tasks_folder_path,
                                output_type=Pools,
                                model_name="llama3",
                                task_name="\\Pools and Swimlanes\\extract.json",
                                mapping_error_tolerance=2,
                                generating_error_tolerance=2)

    pools_and_swimlanes_mapper_config = MapperConfig(schema_descriptor="a Pools object has a list of Pool each Pool has a name and a list of Swimlanes each Swimlane has a name",
                                binding_type=Pools,
                                llm_factory=OllamaFactory(),
                                model_name="codegemma")

    pools_and_swimlanes_extraction_instance = LLMTask(task_config=pools_and_swimlanes_task_config,
                                        mapper_config=pools_and_swimlanes_mapper_config)
    return pools_and_swimlanes_extraction_instance


def create_activities_from_pools_and_swimlanes_extraction_task():

    activities_from_pools_and_swimlanes_task_config = TaskConfig(llm_factory=OllamaFactory(),
                                tasks_folder_path=tasks_folder_path,
                                output_type=Activities,
                                model_name="llama3",
                                task_name="\\Activities from Pools\\extract.json",
                                mapping_error_tolerance=2,
                                generating_error_tolerance=2)

    activities_from_pools_and_swimlanes_mapper_config = MapperConfig(schema_descriptor="an Activities object has a list of Activity each Activity has name, pool and swimlane",
                                binding_type=Activities,
                                llm_factory=OllamaFactory(),
                                model_name="codegemma")


    activities_from_pools_and_swimlanes_extraction_instance = LLMTask(task_config=activities_from_pools_and_swimlanes_task_config,
                                        mapper_config=activities_from_pools_and_swimlanes_mapper_config)
    
    return activities_from_pools_and_swimlanes_extraction_instance





def create_process_description_simplification_extraction_task():

    task_config = TaskConfig(llm_factory=OllamaFactory(),
                                tasks_folder_path=tasks_folder_path,
                                output_type=ProcessDescription,
                                model_name="llama3",
                                task_name="\\Process Description Simplification\\simplify.json",
                                mapping_error_tolerance=2,
                                generating_error_tolerance=2)

    mapper_config = MapperConfig(schema_descriptor="a ProcessDescription object has content",
                                binding_type=ProcessDescription,
                                llm_factory=OllamaFactory(),
                                model_name="codegemma")


    extraction_instance = LLMTask(task_config=task_config,
                                        mapper_config=mapper_config)
    
    return extraction_instance




def create_activities_relationships_extraction_task():

    task_config = TaskConfig(llm_factory=OllamaFactory(),
                                tasks_folder_path=tasks_folder_path,
                                output_type=ActivityRelationShipsList,
                                model_name="llama3",
                                task_name="\\Activities Relationships\\extract.json",
                                mapping_error_tolerance=0,
                                generating_error_tolerance=0)

    mapper_config = MapperConfig(schema_descriptor="an object contains a list of NextActivity named next_activities which contains each NextActivity contains name and condition if there is a null convert it to empty string",
                                binding_type=ActivityRelationShipsList,
                                llm_factory=OllamaFactory(),
                                model_name="codegemma")


    extraction_instance = LLMTask(task_config=task_config,
                                        mapper_config=mapper_config)
    
    return extraction_instance
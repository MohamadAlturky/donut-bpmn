import os
from models.pools_and_swimlanes.model import Pools
from core.design.task import LLMTask
from core.design.config import TaskConfig
from mapping.model.config import MapperConfig
from utils.ollama_factory import OllamaFactory
from dotenv import load_dotenv
from settings import env


load_dotenv(override=True)
tasks_folder_path = os.getenv(env.TASKS_FOLDER_PATH)

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

pools_and_swimlanes_extraction = LLMTask(task_config=pools_and_swimlanes_task_config,
                                    mapper_config=pools_and_swimlanes_mapper_config)

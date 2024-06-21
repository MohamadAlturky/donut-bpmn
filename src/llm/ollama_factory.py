import os
from llm.factory import LLMFactory
from langchain_community.llms import Ollama
from dotenv import load_dotenv
from settings import env

"""
    Returns llm instance. 
"""
class OllamaFactory(LLMFactory):
    def __init__(self):
        load_dotenv(override=True)
        self.host =  os.getenv(env.OLLAMA_HOST)
        self.model_name = os.getenv(env.LLAMA3_MODEL_NAME)
    
    def create(self, model_name : str = None):
        if model_name is None:
            return Ollama(model=self.model_name, base_url=self.host)
        else:
            return Ollama(model=model_name, base_url=self.host)



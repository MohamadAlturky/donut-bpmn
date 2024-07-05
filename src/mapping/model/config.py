class MapperConfig:
    def __init__(self, schema_descriptor, binding_type,
                 model_name, llm_factory):
        self.schema_descriptor = schema_descriptor
        self.binding_type = binding_type 
        self.model_name = model_name
        self.llm_factory = llm_factory

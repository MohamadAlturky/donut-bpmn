class TaskConfig:
    def __init__(self, llm_factory, tasks_folder_path,
                 output_type, model_name,task_name,
                 mapping_error_tolerance,generating_error_tolerance):
        self.llm_factory = llm_factory
        self.tasks_folder_path = tasks_folder_path
        self.output_type = output_type
        self.model_name = model_name
        self.task_name = task_name
        self.mapping_error_tolerance = mapping_error_tolerance
        self.generating_error_tolerance = generating_error_tolerance 
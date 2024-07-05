import json
from core.spec.model.task_spec import TaskSpecification

def load_task_specification(file_path) -> TaskSpecification:
    # print(f"\nloading task specification from {file_path}\n")
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
            # print(f"data loaded from file {file_path}\n{data}\n")
            task = TaskSpecification(**data)
            # print(f"the task description loaded from file {file_path}\n")
            # print(f"backstory: {task.backstory}\n")
            # print(f"description: {task.description}\n")
            # print(f"role: {task.role}\n")
            # print(f"goal: {task.goal}\n")
            # print(f"expected_output: {task.expected_output}\n")

        return task
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
    except json.JSONDecodeError:
        print(f"Error: The file at {file_path} is not a valid JSON file.")
    except TypeError as e:
        print(f"Error: Type mismatch when creating task object: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

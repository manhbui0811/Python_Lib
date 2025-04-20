import json
import importlib

def load_jobs_from_config(config_path):
    with open(config_path, "r") as f:
        config = json.load(f)
    return config.get("jobs", [])

def get_function_from_path(func_path: str):
    """Import hàm từ chuỗi 'module.submodule.function'"""
    module_path, func_name = func_path.rsplit('.', 1)
    module = importlib.import_module(module_path)
    return getattr(module, func_name)

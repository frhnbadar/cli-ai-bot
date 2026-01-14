import os
import importlib

TOOLS = {}
TOOL_INFO = {}

def load_plugins():
    plugins_path = os.path.join(os.path.dirname(__file__), "plugins")

    for filename in os.listdir(plugins_path):
        if filename.endswith(".py") and not filename.startswith("_"):
            module_name = filename[:-3]
            module = importlib.import_module(f"bot.plugins.{module_name}")

            if hasattr(module, "run"):
                TOOLS[module_name] = module.run
                TOOL_INFO[module_name] = getattr(
                    module, "INFO", "No description provided"
                )
print("Loaded tools:", TOOLS.keys())
load_plugins()

def list_tools():
    return "\n".join(f"{k}: {v}" for k, v in TOOL_INFO.items())

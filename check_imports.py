import sys
import traceback

def check_import(module_name):
    try:
        print(f"Checking {module_name}...", end=" ")
        __import__(module_name)
        print("OK")
        return True
    except Exception as e:
        print("FAILED")
        traceback.print_exc()
        return False

modules = [
    "app.api",
    "app.models",
    "app.schemas",
    "app.services.cost_service",
    "integrations.standard_email",
    "integrations.local_llm",
    "integrations.gemini_service",
    "integrations.llm_wrapper",
    "integrations.storage",
    "agent.graph",
    "main"
]

success = True
for mod in modules:
    if not check_import(mod):
        success = False

if not success:
    sys.exit(1)

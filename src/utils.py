import traceback
import os

def mkdir():
    path = "logs"
    if not os.path.exists(path):
        try:
            os.mkdir(path)
        except Exception as Error:
            print(f"ERROR: Wasn't possible to create new folder \"{path}\"")
            print(traceback.format_exc())
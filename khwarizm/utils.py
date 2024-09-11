import os
from pathlib import Path
import logging

def enviroment_setup(project_name:str):
    
    logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

    list_of_files = [
        f"{project_name}/data",
        f"{project_name}/notebooks",
        f"{project_name}/src/data",  
        f"{project_name}/src/models",
        f"{project_name}/src/evaluation",
        f"{project_name}/src/inference",
        f"{project_name}/src/utils",
        f"{project_name}/src/tests",
        "requirements.txt",
        "README.md",
        ".gitignore"
    ]

    for filepath in list_of_files: 
        filepath = Path(filepath) #it solves the / slash and \ slash problem internally
        filedir, filename = os.path.split(filepath)
        if filedir != "":
            os.makedirs(filedir,exist_ok=True)
        if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0): 
            with open (filepath, "w") as f:
                pass
        else:
            print(f"file path is already present at :{filepath}")
            
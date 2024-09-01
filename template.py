import os
from pathlib import Path 
 
project_name = "khwarizm"

list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/src/khwarizm/__init__.py",
    f"{project_name}/src/khwarizm/preprocessing.py",  
    f"{project_name}/src/khwarizm/metrics.py",
    f"{project_name}/src/khwarizm/ensembles.py",
    f"{project_name}/src/khwarizm/feature_selection.py",
    f"{project_name}/src/khwarizm/utils.py",
    f"{project_name}/src/khwarizm/logs.py",
    f"{project_name}/src/khwarizm/reports.py",
    f"{project_name}/tests/__init__.py",
    f"{project_name}/tests/test_preprocessing.py",
    f"{project_name}/tests/test_metrics.py",
    f"{project_name}/tests/test_ensembles.py",
    f"{project_name}/tests/test_feature_selection.py",
    f"{project_name}/tests/test_logs.py",
    f"{project_name}/tests/test_reports.py"
    "requirements.txt",
    "setup.py",
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
        
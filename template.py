"""import os

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        
def create_file(path, content=''):
    with open(path, 'w') as file:
        file.write(content)
        
def create_project_structure():
    root = 'khwarizm'
    create_directory(root)
    
    #hte root level files 
    create_file(os.path.join(root, 'gitignore'))
    create_file(os.path.join(root, 'README.md'))
    create_file(os.path.join(root, 'requirements.txt'))
    create_file(os.path.join(root, 'setup.py'))
    
    src_dir = os.path.join(root,'src')
    create_directory(src_dir)
    
    """
    
    
import os
from pathlib import Path 
 
project_name = "khwarizm"

list_of_files = [
    f"{project_name}/__init__.py",
    f"{project_name}/src/khwarizm/__init__.py",
    f"{project_name}/src/khwarizm/preprocessing.py",  
    f"{project_name}/src/khwarizm/metrics.py",
    f"{project_name}/src/khwarizm/ensembles.py",
    f"{project_name}/src/khwarizm/utils.py",
    f"{project_name}/src/khwarizm/logs.py",
    f"{project_name}/src/khwarizm/reports.py",
    f"{project_name}/tests/__init__.py",
    f"{project_name}/tests/test_preprocessing.py",
    f"{project_name}/tests/test_metrics.py",
    f"{project_name}/tests/test_ensembles.py",
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
        
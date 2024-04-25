import os
from pathlib import Path


list_of_folders = [

"src/__init__.py",
"src/components/__init__.py",
"src/components/data_ingestions.py",
"src/components/data_transformation.py",
"src/components/model_trainer.py",
"src/components/model_evaluation.py",
"src/pipeline/__init__.py",
"src/pipeline/prediction_pipeline.py",
"src/pipeline/training_pipeline.py",
"src/pipeline/batch_prediction.py",
"src/logging/__init__.py",
"src/logging/logging.py",
"src/exception/__init__.py",
"src/exception/exception.py",
"src/utils/__init__.py",
"src/utils/utils.py",
"templates/form.html",
"templates/index.html",
"templates/result.html",
"test/__init__.py",
"test/integration/__init__.py",
"test/integration/integration.py",
"test/unit/__init__.py",
"test/unit/unit.py",
"app.py",
"Dockerfile",
"Dockerfile.airflow",
"Dockerfile.flask",
"init_setup.sh",
"setup.py",
"setup.cfg",
"requirements_dev.txt",
"requirements.txt",
"start.sh",
"tox.ini",
"dvc.yaml",
"test.py",
"pyproject.toml",
"Artifacts",
".github/workflows",
"airflow/dags"

]

for filepath in list_of_folders:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # create an empty file

#its updated
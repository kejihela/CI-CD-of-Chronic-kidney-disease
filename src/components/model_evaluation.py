import pandas as pd
import numpy as np
from src.logging.logging import logging
from src.exception.exception import customexception
from sklearn.metrics import accuracy_score, recall_score, f1_score, precision_score
import mlflow
import mlflow.sklearn
from urllib.parse import urlparse

import os
import sys
from sklearn.model_selection import train_test_splits
from dataclasses import dataclass
from pathlib import Path

@dataclass
class ModelEvaluation:
    pass
class ModelEvaluaion:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        try:
            pass
        except Exception as e:
            logging.info()
            raise customexception(e,sys)


    
import os
import sys
import pickle
import numpy as np
import pandas as pd
from src.logging.logging import logging
from src.exception.exception import customexception
from src.utils.utils import save_object

from sklearn.metrics import accuracy_score, precision_score, f1_score, recall_score

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise customexception(e,sys)

def evaluate_model(X_train, y_train, X_test, y_test, models):
    try:
        report = {}
        for i in range(len(models)):
            model = list(models.values())[i]
            model.fit(X_train, y_train)

            y_test_pred = model.predict(X_test)

            test_model_score = accuracy_score(y_test, y_test_pred)

            report[list(models.key())[i]] = test_model_score

        return report

    except Exception as e:
        logging.info("Exception occured during model  training")
        raise customexception(e, sys)



def load_object(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_path)
    except Exception as e:
        logging.info("Exception occured in load object function")
        raise customexception(e, sys)

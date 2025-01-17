import os
import sys
import pickle
import numpy as np
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

def save_object(file_path, obj):
    """
    Saves a Python object to a file using pickle.

    Args:
        file_path (str): The path to save the object.
        obj: The object to be saved.

    Raises:
        CustomException: If an error occurs during saving.
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e, sys)

def evaluate_model(X_train, y_train, X_test, y_test, models):
    """
    Evaluates the performance of multiple machine learning models.

    Args:
        X_train (np.array or pd.DataFrame): Training features.
        y_train (np.array or pd.Series): Training labels.
        X_test (np.array or pd.DataFrame): Test features.
        y_test (np.array or pd.Series): Test labels.
        models (dict): A dictionary of model names and model objects.

    Returns:
        dict: A dictionary containing R2 scores for each model.

    Raises:
        CustomException: If an error occurs during model evaluation.
    """
    try:
        report = {}
        for model_name, model in models.items():
            # Train the model
            model.fit(X_train, y_train)

            # Predict on the test data
            y_test_pred = model.predict(X_test)

            # Calculate R2 score for the test data
            test_model_score = r2_score(y_test, y_test_pred)

            # Store the score in the report dictionary
            report[model_name] = test_model_score

        return report
    except Exception as e:
        logging.info('Exception occurred during model training')
        raise CustomException(e, sys)

def load_object(file_path):
    """
    Loads a Python object from a file using pickle.

    Args:
        file_path (str): The path to the file.

    Returns:
        obj: The loaded object.

    Raises:
        CustomException: If the file does not exist or an error occurs during loading.
    """
    try:
        if not os.path.exists(file_path):
            raise CustomException(f"File not found: {file_path}", sys)

        with open(file_path, 'rb') as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        logging.info('Exception occurred in load_object function in utils')
        raise CustomException(e, sys)

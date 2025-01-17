import os  # Provides functions for interacting with the operating system.
import sys  # Allows access to system-specific parameters and functions.
from src.logger import logging  # Custom module for logging events and processes.
from src.exception import CustomException  # Custom module for handling exceptions.
import pandas as pd  # Library for data manipulation and analysis.

# Importing custom components for the data pipeline.
from src.components.data_ingestion import DataIngestion  # Handles data reading and splitting.
from src.components.data_transformation import DataTransformation  # Handles data preprocessing.
from src.components.model_trainer import ModelTrainer  # Handles model training.

# Entry point of the script.
if __name__ == '__main__':
    # Step 1: Data Ingestion
    obj = DataIngestion()  # Create an instance of the DataIngestion class.
    train_data_path, test_data_path = obj.initiate_data_ingestion()  # Ingest data and get paths for train/test data.
    print(train_data_path, test_data_path)  # Display paths of the train and test datasets.

    # Step 2: Data Transformation
    data_transformation = DataTransformation()  # Create an instance of the DataTransformation class.
    # Perform data transformation and return transformed train and test arrays.
    train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data_path, test_data_path)

    # Step 3: Model Training
    model_trainer = ModelTrainer()  # Create an instance of the ModelTrainer class.
    # Train the model using the transformed train and test datasets.
    model_trainer.initate_model_training(train_arr, test_arr)

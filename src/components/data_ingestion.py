import os  # Module for interacting with the operating system (e.g., file paths, directories).
import sys  # Provides system-specific parameters and functions.
from src.logger import logging  # Custom logging module for logging events.
from src.exception import CustomException  # Custom exception class for handling errors.
import pandas as pd  # Library for data manipulation and analysis.
from sklearn.model_selection import train_test_split  # Function to split data into training and testing sets.
from dataclasses import dataclass  # Simplifies the creation of data classes for managing data.

# Define a configuration class for data ingestion.
@dataclass
class DataIngestionconfig:
    # Paths for storing train, test, and raw data.
    train_data_path = os.path.join('artifacts', 'train.csv')  # Path for training data.
    test_data_path = os.path.join('artifacts', 'test.csv')  # Path for testing data.
    raw_data_path = os.path.join('artifacts', 'raw.csv')  # Path for raw data.

# Define a data ingestion class to manage the data ingestion process.
class DataIngestion:
    def __init__(self):
        # Initialize the configuration for data ingestion.
        self.ingestion_config = DataIngestionconfig()

    def initiate_data_ingestion(self):
        """
        Reads raw data, splits it into training and testing sets, 
        and saves the data to specified file paths.
        """
        logging.info('Data Ingestion method starts')  # Log the start of data ingestion.

        try:
            # Read the raw dataset from a specified path.
            df = pd.read_csv(os.path.join('notebooks/data', 'gemstone.csv'))
            logging.info('Dataset read as pandas DataFrame')  # Log successful data reading.

            # Create the directory for saving raw data if it doesn't already exist.
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path), exist_ok=True)

            # Save the raw data to a CSV file.
            df.to_csv(self.ingestion_config.raw_data_path, index=False)

            logging.info("Train test split")  # Log the train-test split process.
            
            # Split the dataset into training and testing sets.
            train_set, test_set = train_test_split(df, test_size=0.30, random_state=42)

            # Save the training and testing data to their respective CSV files.
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info('Ingestion of data is completed')  # Log completion of data ingestion.

            # Return the file paths for train and test datasets.
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            # Handle any exceptions that occur during data ingestion.
            logging.info('Error occurred in Data Ingestion config')
            raise CustomException(e, sys)  # Raise a custom exception with the error details.

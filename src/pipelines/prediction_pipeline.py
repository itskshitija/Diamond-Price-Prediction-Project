# Import necessary libraries and modules
import sys  # Provides access to system-specific parameters and functions
import os  # Used for interacting with the operating system
from src.exception import CustomException  # Custom exception class for handling errors
from src.logger import logging  # Custom logging module for logging information
from src.utils import load_object  # Utility function to load serialized objects (e.g., pickled files)
import pandas as pd  # Library for working with data in DataFrame format

class PredictPipeline:
    """
    Handles the prediction process by utilizing pre-trained model and preprocessor artifacts.
    """
    def __init__(self):
        pass

    def predict(self, features):
        """
        Make predictions using a pre-trained model and preprocessor.

        Args:
            features (DataFrame or array-like): Input data to predict on.

        Returns:
            pred (array-like): Predictions from the model.
        """
        try:
            # Define file paths for the preprocessor and model artifacts
            preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')
            model_path = os.path.join('artifacts', 'model.pkl')

            logging.info(f"Loading preprocessor from {preprocessor_path} and model from {model_path}.")

            # Load the preprocessor and model
            preprocessor = load_object(preprocessor_path)
            model = load_object(model_path)

            logging.info("Successfully loaded preprocessor and model.")

            # Transform the input features using the preprocessor
            data_scaled = preprocessor.transform(features)
            logging.info("Data transformation completed successfully.")

            # Make predictions using the model
            pred = model.predict(data_scaled)
            logging.info("Prediction completed successfully.")
            
            return pred

        except Exception as e:
            logging.error("Exception occurred during prediction: %s", str(e))
            raise CustomException(e, sys)


class CustomData:
    """
    Represents custom input data for prediction.
    """
    def __init__(self,
                 carat: float,
                 depth: float,
                 table: float,
                 x: float,
                 y: float,
                 z: float,
                 cut: str,
                 color: str,
                 clarity: str):
        """
        Initialize the attributes for custom data input.

        Args:
            carat (float): Weight of the diamond.
            depth (float): Depth percentage.
            table (float): Width of the diamond's table.
            x (float): Length in mm.
            y (float): Width in mm.
            z (float): Height in mm.
            cut (str): Quality of the cut.
            color (str): Color grade.
            clarity (str): Clarity grade.
        """
        self.carat = carat
        self.depth = depth
        self.table = table
        self.x = x
        self.y = y
        self.z = z
        self.cut = cut
        self.color = color
        self.clarity = clarity

    def get_data_as_dataframe(self):
        """
        Convert the custom data into a Pandas DataFrame format for model prediction.

        Returns:
            pd.DataFrame: A DataFrame containing the input data.
        """
        try:
            # Create a dictionary to hold the input data
            custom_data_input_dict = {
                'carat': [self.carat],
                'depth': [self.depth],
                'table': [self.table],
                'x': [self.x],
                'y': [self.y],
                'z': [self.z],
                'cut': [self.cut],
                'color': [self.color],
                'clarity': [self.clarity]
            }

            # Convert the dictionary to a Pandas DataFrame
            df = pd.DataFrame(custom_data_input_dict)
            logging.info('DataFrame created successfully.')

            # Optional: Ensure the DataFrame has the correct column order (if needed for model input)
            expected_columns = ['carat', 'depth', 'table', 'x', 'y', 'z', 'cut', 'color', 'clarity']
            if list(df.columns) != expected_columns:
                logging.warning(f"Column order mismatch. Expected columns: {expected_columns}, Found: {list(df.columns)}")
            
            return df

        except Exception as e:
            logging.error('Exception occurred in get_data_as_dataframe method: %s', str(e))
            raise CustomException(e, sys)

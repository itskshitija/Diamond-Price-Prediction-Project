from sklearn.impute import SimpleImputer  # Handles missing values by imputing them with median or most frequent values.
from sklearn.preprocessing import StandardScaler  # Performs feature scaling (standardization of numerical features).
from sklearn.preprocessing import OrdinalEncoder  # Encodes categorical data with a specified ordinal order.
from sklearn.pipeline import Pipeline  # Helps streamline a series of data processing steps.
from sklearn.compose import ColumnTransformer  # Applies different transformations to different columns of the dataset.
import sys, os  # For system-level operations and path handling.
from dataclasses import dataclass  # Used to define classes with less boilerplate code for storing configuration.
import pandas as pd  # For data manipulation and analysis.
import numpy as np  # For numerical operations.

from src.exception import CustomException  # A custom exception handler defined elsewhere in the project.
from src.logger import logging  # Custom logging utility for better tracking of the code's progress.
from src.utils import save_object  # Utility function to save objects (e.g., preprocessors) for future use.


@dataclass
class DataTransformationconfig:
    preprocessor_obj_file_path = os.path.join('artifacts', 'preprocessor.pkl')  
    # Path to save the serialized preprocessor object.


class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationconfig()  
        # Initializes the transformation configuration.

    def get_data_transformation_object(self):
        """
        Creates and returns a preprocessor object for handling data transformation.
        """
        try:
            logging.info('Data Transformation initiated')

            # Define columns for transformations.
            categorical_cols = ['cut', 'color', 'clarity']  # Columns with categorical data.
            numerical_cols = ['carat', 'depth', 'table', 'x', 'y', 'z']  # Columns with numerical data.

            # Define ranking for ordinal encoding of categorical variables.
            cut_categories = ['Fair', 'Good', 'Very Good', 'Premium', 'Ideal']
            color_categories = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
            clarity_categories = ['I1', 'SI2', 'SI1', 'VS2', 'VS1', 'VVS2', 'VVS1', 'IF']

            logging.info('Pipeline Initiated')

            # Define numerical pipeline: handles missing values and scales numerical data.
            num_pipeline = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='median')),  # Fill missing values with the median.
                ('scaler', StandardScaler())  # Standardize features.
            ])

            # Define categorical pipeline: handles missing values, encodes, and scales categorical data.
            cat_pipeline = Pipeline(steps=[
                ('imputer', SimpleImputer(strategy='most_frequent')),  # Fill missing values with the most frequent value.
                ('ordinalencoder', OrdinalEncoder(categories=[cut_categories, color_categories, clarity_categories])),
                ('scaler', StandardScaler())  # Standardize features.
            ])

            # Combine the two pipelines into a column transformer.
            preprocessor = ColumnTransformer([
                ('num_pipeline', num_pipeline, numerical_cols),
                ('cat_pipeline', cat_pipeline, categorical_cols)
            ])

            return preprocessor  # Returns the preprocessor object.

            logging.info('Pipeline Completed')
        except Exception as e:
            logging.info("Error in Data Transformation")
            raise CustomException(e, sys)

    def initiate_data_transformation(self, train_path, test_path):
        """
        Reads training and testing datasets, applies the transformation, and saves the preprocessor.
        """
        try:
            # Read train and test datasets.
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info('Read train and test data completed')
            logging.info(f'Train Dataframe Head : \n{train_df.head().to_string()}')
            logging.info(f'Test Dataframe Head  : \n{test_df.head().to_string()}')

            logging.info('Obtaining preprocessing object')

            preprocessing_obj = self.get_data_transformation_object()  # Get the preprocessor.

            # Define the target column and columns to drop.
            target_column_name = 'price'
            drop_columns = [target_column_name, 'id']

            # Split features into independent (X) and dependent (y).
            input_feature_train_df = train_df.drop(columns=drop_columns, axis=1)
            target_feature_train_df = train_df[target_column_name]

            input_feature_test_df = test_df.drop(columns=drop_columns, axis=1)
            target_feature_test_df = test_df[target_column_name]

            # Apply preprocessing to train and test datasets.
            input_feature_train_arr = preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessing_obj.transform(input_feature_test_df)

            logging.info("Applying preprocessing object on training and testing datasets.")

            # Combine transformed features with the target variable.
            train_arr = np.c_[input_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            # Save the preprocessor object to disk.
            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )

            logging.info('Processor pickle is created and saved.')

            return train_arr, test_arr, self.data_transformation_config.preprocessor_obj_file_path
        except Exception as e:
            logging.info("Exception occurred in the initiate_data_transformation")
            raise CustomException(e, sys)

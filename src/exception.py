# Import necessary modules
import sys  # Provides access to system-specific parameters and functions
from src.logger import logging  # Imports a custom logging setup (assumed to be defined elsewhere)

# Function to extract and format error details
def error_message_detail(error, error_detail: sys):
    """
    Captures detailed error information, including:
    - The file where the error occurred
    - The line number of the error
    - The error message
    """
    try:
        # Extract traceback object, which provides information about the error
        _, _, exc_tb = error_detail.exc_info()

        # Check if the traceback object is valid
        if exc_tb is not None:
            # Get the filename where the exception occurred
            file_name = exc_tb.tb_frame.f_code.co_filename
            # Format the error details into a human-readable message
            error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
                file_name, exc_tb.tb_lineno, str(error)
            )
        else:
            # Handle the case where traceback is None
            error_message = "Error occurred, but no traceback available: [{0}]".format(str(error))
    
    except Exception as e:
        # If there is an error while processing the exception, log the error
        error_message = f"Error in error handling: {str(e)}"

    return error_message  # Return the formatted error message

# Custom exception class for enhanced error reporting
class CustomException(Exception):
    """
    Custom exception class that:
    - Extends Python's built-in Exception class
    - Adds functionality to capture detailed error information
    """

    def __init__(self, error_message, error_detail: sys):
        """
        Constructor that takes the error message and system details to build a detailed error report.
        """
        super().__init__(error_message)  # Initialize the parent Exception class
        # Generate detailed error information using the `error_message_detail` function
        self.error_message = error_message_detail(error_message, error_detail=error_detail)

    def __str__(self):
        """
        Returns the detailed error message when the exception is printed.
        """
        return self.error_message

# Main section of the code
if __name__ == "__main__":
    # Log a startup message
    logging.info("Logging has started")

    try:
        # Example code that causes a division-by-zero error
        a = 1 / 0
    except Exception as e:
        # Log the specific error encountered
        logging.info("Division by zero")
        # Raise a custom exception with detailed error information
        raise CustomException(e, sys)

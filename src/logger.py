# Import necessary modules
import logging  # Provides a way to track events that happen during program execution
import os       # Helps interact with the operating system, e.g., managing file paths
from datetime import datetime  # Used for fetching the current date and time

# Generate a log file name with a timestamp (e.g., "01_16_2025_14_30_45.log")
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the directory path where log files will be stored
# This combines the current working directory with a folder named 'logs' and the log file name
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# Create the 'logs' directory if it doesn't already exist
os.makedirs(logs_path, exist_ok=True)

# Define the complete path for the log file (directory + file name)
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Configure the logging settings
logging.basicConfig(
    filename=LOG_FILE_PATH,  # The log file where logs will be written
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s", 
    # Log message format:
    # - %(asctime)s: Timestamp of the log entry
    # - %(lineno)d: Line number in the code where the log was called
    # - %(name)s: Logger name
    # - %(levelname)s: Severity level of the log (e.g., INFO, DEBUG, WARNING)
    # - %(message)s: The log message provided by the developer
    level=logging.INFO  # Set the logging level to INFO (logs INFO and more critical levels)
)

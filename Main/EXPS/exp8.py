import logging
import os
from datetime import datetime

def setup_logging():
   # Create logs directory if it doesn't exist
   log_dir = "logs"
   if not os.path.exists(log_dir):
      os.makedirs(log_dir)
   
   # Create a custom logger
   logger = logging.getLogger("LearnLogging")
   logger.setLevel(logging.DEBUG)  # Set the lowest level to capture all logs
   
   # Clear any existing handlers to avoid duplicates
   logger.handlers.clear()
   
   # Create formatters
   detailed_formatter = logging.Formatter(
      '%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s',
      datefmt='%Y-%m-%d %H:%M:%S'
   )
   
   simple_formatter = logging.Formatter(
      '%(levelname)s - %(message)s'
   )
   
   # File handler - saves all logs to file
   file_handler = logging.FileHandler(
      os.path.join(log_dir, f"app_{datetime.now().strftime('%Y%m%d')}.log"),
      encoding='utf-8'
   )
   file_handler.setLevel(logging.DEBUG)
   file_handler.setFormatter(detailed_formatter)
   
   # Console handler - shows only INFO and above to console
   console_handler = logging.StreamHandler()
   console_handler.setLevel(logging.INFO)
   console_handler.setFormatter(simple_formatter)
   
   # Error file handler - saves only errors to separate file
   error_handler = logging.FileHandler(
      os.path.join(log_dir, f"errors_{datetime.now().strftime('%Y%m%d')}.log"),
      encoding='utf-8'
   )
   error_handler.setLevel(logging.ERROR)
   error_handler.setFormatter(detailed_formatter)
   
   # Add handlers to logger
   logger.addHandler(file_handler)
   logger.addHandler(console_handler)
   logger.addHandler(error_handler)
   
   return logger

def demonstrate_log_levels(logger):
    """
    Demonstrate different logging levels:
    DEBUG: Detailed information for diagnosing problems
    INFO: General information about program execution
    WARNING: Something unexpected happened, but the program still works
    ERROR: A serious problem occurred
    CRITICAL: A very serious error occurred
    """
    
    logger.debug("This is a DEBUG message - detailed diagnostic info")
    logger.info("This is an INFO message - general program flow")
    logger.warning("This is a WARNING message - something unexpected but not critical")
    logger.error("This is an ERROR message - something went wrong")
    logger.critical("This is a CRITICAL message - serious problem!")

def simulate_operations(logger):
    """
    Simulate various operations with appropriate logging
    """
    
    logger.info("Starting application operations")
    
    # Simulate user login
    username = "john_doe"
    logger.info(f"User {username} attempting to log in")
    
    try:
        # Simulate some processing
        logger.debug("Processing user authentication")
        
        # Simulate successful login
        logger.info(f"User {username} successfully logged in")
        
        # Simulate some business logic
        logger.debug("Executing business logic")
        
        # Simulate a warning condition
        if datetime.now().hour > 22:
            logger.warning("User accessing system after hours")
        
        # Simulate processing data
        data_count = 150
        logger.info(f"Processing {data_count} records")
        
        for i in range(1, 6):  # Process 5 records as example
            logger.debug(f"Processing record {i}")
            
            # Simulate an occasional error
            if i == 3:
                logger.error(f"Failed to process record {i} - invalid data format")
                continue
            
            logger.debug(f"Successfully processed record {i}")
        
        logger.info("Data processing completed")
        
    except Exception as e:
        logger.critical(f"Critical error in operations: {e}")
        raise
    
    finally:
        logger.info("Cleaning up resources")

def demonstrate_exception_logging(logger):
    """
    Demonstrate proper exception logging
    """
    
    logger.info("Demonstrating exception logging")
    
    try:
        # Simulate an operation that might fail
        result = 10 / 0  # This will raise ZeroDivisionError
        
    except ZeroDivisionError as e:
        # Log the exception with traceback
        logger.error("Division by zero error occurred", exc_info=True)
        
        # Alternative way to log exceptions
        logger.exception("This automatically includes the traceback")
        
    except Exception as e:
        # Generic exception handling
        logger.error(f"Unexpected error: {e}", exc_info=True)

def demonstrate_conditional_logging(logger):
    """
    Demonstrate conditional and efficient logging
    """
    
    # Expensive operation that we only want to do if DEBUG is enabled
    if logger.isEnabledFor(logging.DEBUG):
        expensive_debug_info = f"Debug info: {[i**2 for i in range(1000)][:10]}"
        logger.debug(expensive_debug_info)
    
    # Using lazy evaluation for expensive string formatting
    logger.debug("User data: %s", {"user_id": 123, "data": "sensitive_info"})

def main():
   print("=== Python Logging Tutorial ===\n")
   
   # Set up logging
   logger = setup_logging()
   
   logger.info("=" * 50)
   logger.info("LOGGING TUTORIAL STARTED")
   logger.info("=" * 50)
   
   print("1. Demonstrating different log levels:")
   demonstrate_log_levels(logger)
   
   print("\n2. Simulating application operations:")
   simulate_operations(logger)
   
   print("\n3. Demonstrating exception logging:")
   demonstrate_exception_logging(logger)
   
   print("\n4. Demonstrating conditional logging:")
   demonstrate_conditional_logging(logger)
   
   logger.info("=" * 50)
   logger.info("LOGGING TUTORIAL COMPLETED")
   logger.info("=" * 50)
   
   print(f"\nCheck the 'logs' directory for generated log files:")
   print(f"- app_{datetime.now().strftime('%Y%m%d')}.log (all logs)")
   print(f"- errors_{datetime.now().strftime('%Y%m%d')}.log (errors only)")

if __name__ == "__main__":
   main()
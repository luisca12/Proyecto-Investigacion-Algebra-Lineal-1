from src.log import logConfiguration

import logging.config
import traceback

infoLog = logging.getLogger('infoLog')

def checkIsDigit(input_str):
    """
    This function checks if the provided string is a digit.

    **Args:**
        input_str: The string to be checked.
        
    **Returns:**
        bool: True if the string is a digit, False otherwise.
    """
    try:
        input_str = input_str.strip()
        infoLog.info(f"String successfully validated selection number {input_str}, from checkIsDigit function.")
        return input_str.isdigit()
    
    except Exception as error:
        infoLog.error(f"Invalid option chosen: {input_str}, error: {error}")
        infoLog.error(traceback.format_exc())
import re

def escape_special_characters(input_string):
    """
    Escapes special SQL characters in a string input.
    
    Args:
    input_string (str): The input string to sanitize.
    
    Returns:
    str: The sanitized string with special SQL characters escaped.
    """
    special_chars = {'\'': '\\\'', '\"': '\\\"', '\0': '\\0', '\b': '\\b', '\n': '\\n', '\r': '\\r', '\t': '\\t', '\\': '\\\\', '%': '\\%', '_': '\\_'}
    for char, escaped_char in special_chars.items():
        input_string = input_string.replace(char, escaped_char)
    return input_string

def validate_integer(input_value):
    """
    Validates if the input value is an integer.
    
    Args:
    input_value: The input value to validate.
    
    Returns:
    bool: True if the input is an integer, False otherwise.
    """
    try:
        int(input_value)
        return True
    except ValueError:
        return False

def validate_email(input_email):
    """
    Validates if the input string is a valid email format.
    
    Args:
    input_email (str): The input email to validate.
    
    Returns:
    bool: True if the input is a valid email, False otherwise.
    """
    if re.match(r"[^@]+@[^@]+\.[^@]+", input_email):
        return True
    else:
        return False
    
def validate_url(input_url):
    """
    Validates if the input string is a valid URL format.
    
    Args:
    input_url (str): The input URL to validate.
    
    Returns:
    bool: True if the input is a valid URL, False otherwise.
    """
    if re.match(r"https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+", input_url):
        return True
    else:
        return False

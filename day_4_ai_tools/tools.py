import secrets
import string

def get_curr_dateTime():
    """
    Get the current date and time in the format YYYY-MM-DD HH:MM:SS.

    Returns:
        str: The current date and time as a string.
    """
    from datetime import datetime
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def roll_dice():
    """
    Simulate rolling a six-sided die.

    Returns:
        int: A random integer between 1 and 6, inclusive.
    """
    import random
    return random.randint(1, 6)

def generate_password(length=12):
    """ Generate a secure random password of specified length. """
    characters = (
        string.ascii_letters + string.digits + string.punctuation
    )
    password = ""
    for _ in range(length):
        password += secrets.choice(characters)
    return password

print("Current Date and Time:", get_curr_dateTime())
print("Rolling a die:", roll_dice())
print("Generated Password:", generate_password())
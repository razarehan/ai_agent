import random
import secrets
import string

from fastmcp import FastMCP
from datetime import datetime

mcp = FastMCP(
  "Time server"
)

@mcp.tool()
def current_time():
  """
  Return the current date and time as a string.
  """
  return datetime.now().strftime("%d-%m-%Y %H:%M:%S")

@mcp.tool()
def roll_dice():
    """
    Simulate rolling a six-sided die.

    Returns:
        int: A random integer between 1 and 6, inclusive.
    """
    return random.randint(1, 6)

@mcp.tool()
def generate_password(length=12):
    """ Generate a secure random password of specified length. """
    characters = (
        string.ascii_letters + string.digits + string.punctuation
    )
    password = ""
    for _ in range(length):
        password += secrets.choice(characters)
    return password

if __name__ == "__main__":
  print("Starting MCP server...")
  mcp.run()
from tools import get_curr_dateTime, roll_dice, generate_password
def call_tool(tool_name):
    """
    Call the specified tool and return the result.

    Args:
        tool_name (str): The name of the tool to call.

    Returns:
        The result of the tool call.
    """
    if tool_name == "get_curr_dateTime":
        return get_curr_dateTime()
    elif tool_name == "roll_dice":
        return roll_dice()
    elif tool_name == "generate_password":
        return generate_password()
    else:
        return None
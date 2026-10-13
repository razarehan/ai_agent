import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
model = os.getenv("OPENAI_MODEL")
client = OpenAI(api_key=api_key)

def choose_tool(user_input, tools):
    """
    Choose the appropriate tool based on user input using LLM.

    Args:
        user_input (str): The input provided by the user.
        tools (dict): A dictionary of available tools.

    Returns:
        str: The name of the chosen tool.
    """
    available_tools = generate_tool_description(tools)

    prompt = f"""You are an AI agent, you have given a list of available tools and a user input.
    User Input: {user_input}
    Available Tools: {available_tools}
    Based on the user input, choose the most appropriate tool from the list above.
    Please respond with the name of the chosen tool only.
    If the user input does not match any tool, respond with 'None'.
    """
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "system", "content": prompt}],
        max_tokens=50
    )
    chosen_tool = response.choices[0].message.content.strip()
    return chosen_tool

def generate_tool_description(tools):
    """
    Concatenate the tool's name and description to create a single string.

    Args:
        tools (list): A list of tool objects for which to generate descriptions.

    Returns:
        str: A string containing the tool's name and description.
    """
    tools_description = ""
    for tool in tools:
        tools_description += f"{tool.name}: {tool.description}\n"
    return tools_description
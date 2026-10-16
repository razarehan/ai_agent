import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
model = os.getenv("OPENAI_MODEL")
client = OpenAI(api_key=api_key)

def planner(state, tools):
    """
    Choose the appropriate tool based on state using LLM.

    Args:
        state (dict): A dictionary of user_request, current_step, max_steps, actions, observations, finished, final_answer.
        tools (dict): A dictionary of available tools.

    Returns:
        str: The name of the chosen tool.
    """
    tool_descriptions = generate_tool_description(tools)

    prompt = f"""
    You are an AI Planner.

    Your job is to decide ONLY the next action.

    User Request:
    {state["user_request"]}

    Completed Actions:
    {state["actions"]}

    Previous Observations:
    {state["observations"]}

    Available Tools:
    {tool_descriptions}

    Rules:

    1. Choose only ONE next action.
    2. Never repeat an action that has already been completed.
    3. Use the observations to decide what is still required.
    4. If the user's request has been completely satisfied, return FINISH.
    5. Return ONLY the tool name or FINISH.
    6. Do not explain your answer.

    Next Action:
    """
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "system", "content": prompt}],
        max_tokens=50
    )
    return response.choices[0].message.content.strip()

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
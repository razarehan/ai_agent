import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
model = os.getenv("OPENAI_MODEL")
client = OpenAI(api_key=api_key)

def choose_tool(user_input):
    """
    Choose the appropriate tool based on user input using LLM.

    Args:
        user_input (str): The input provided by the user.

    Returns:
        str: The name of the chosen tool.
    """
    prompt = f"""You are an AI agent that can choose the appropriate tool based on user input. 
    The available tools are:
    1. get_curr_dateTime: Get the current date and time.
    2. roll_dice: Simulate rolling a six-sided die.
    3. generate_password: Generate a secure random password.
    User Input: {user_input}
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
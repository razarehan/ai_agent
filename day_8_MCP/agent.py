import asyncio
import os
from dotenv import load_dotenv
from openai import OpenAI
from planner import choose_tool
from mcp_client import *

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
model = os.getenv("OPENAI_MODEL")
client = OpenAI(api_key=api_key)

messages = []

print("=" * 50)
print("AI Chatbot initialized. Type 'quit' to exit.")
print("=" * 50)

def generate_response(user_input, tool_result):
    """
    Generate a response based on user input and tool result.

    Args:
        user_input (str): The input provided by the user.
        tool_result (str): The result obtained from the tool.

    Returns:
        str: The generated response.
    """

    prompt = f"""
    You are an AI agent that can answer questions based on user input and tool results.
    You are given a tool result and a question.
    Your task is to provide a concise and natural answer.
    question: {user_input}
    tool result: {tool_result}
    """
    messages.append({
        "role": "user",
        "content": prompt
    })
    response = client.chat.completions.create(
        model=model,
        messages=messages
    )
    return response.choices[0].message.content.strip()

async def main():
    # Connect to the MCP server
    mcp_client = await connect()

    # Discover available tools
    tools = await discover_tools(mcp_client)

    while True:
        user_input = input("\nYou: ")
        
        if(user_input.strip() == ""):
            print("Please enter a valid question.")
            continue

        if user_input.lower() == "quit":
            print("Goodbye!")
            break   

        # step 1: Choose the appropriate tool based on user input using LLM
        chosen_tool = choose_tool(user_input, tools)
        
        # step 2: execute the chosen tool if applicable and get the result
        tool_result = await execute_tool(mcp_client, chosen_tool)
        
        # step 3: Generate a response based on user input and tool result using LLM
        final_response = generate_response(user_input, tool_result)
        print(f"AI: {final_response}")

    # Disconnect from the MCP server
    await disconnect(mcp_client)

if __name__ == "__main__":
    asyncio.run(main())
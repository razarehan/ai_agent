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

        # step 1: Check any tool is required to answer the question
        chosen_tool = choose_tool(user_input, tools)
        
        # step 2: If tool is required, call the tool and get the result
        if chosen_tool is not None:
            tool_result = await execute_tool(mcp_client, chosen_tool)
        
        # step 3: If tool is not required, call the LLM to answer the question
        # or If result from tool is available, call the LLM to naturally answer
        if chosen_tool is None:
            prompt = f"""
            You are an AI agent that can answer questions based on user input.
            User Input: {user_input}
            Please provide a concise and accurate answer to the user's question.
            """
        else:
            prompt = f"""
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
        print("AI:", response.choices[0].message.content.strip())

    # Disconnect from the MCP server
    await disconnect(mcp_client)

if __name__ == "__main__":
    asyncio.run(main())
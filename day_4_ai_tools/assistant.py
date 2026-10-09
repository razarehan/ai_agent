import os
from dotenv import load_dotenv
from openai import OpenAI
from tools import get_curr_dateTime, roll_dice, generate_password
from tools_manager import manage_tools

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
model = os.getenv("OPENAI_MODEL")

client = OpenAI(api_key=api_key)
print("=" * 50)
print("AI Chatbot initialized. Type 'quit' to exit.")
print("=" * 50)
conversations = []

while True:
    user_input = input("\nYou: ")
    
    if(user_input.strip() == ""):
        print("Please enter a valid input.")
        continue

    if user_input.lower() == "quit":
        print("Goodbye!")
        break

    tool_response = manage_tools(user_input)
    if tool_response is not None:
        print(f"\nAI: {tool_response}")
        continue

    conversations.append({
        "role": "user",
        "content": user_input
    })
    response = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL"),
        messages=conversations
    )

    conversations.append({
        "role": "assistant", 
        "content": response.choices[0].message.content
    })

    #display the response
    print("\nAI: " + response.choices[0].message.content)
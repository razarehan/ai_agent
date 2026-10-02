import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
model = os.getenv("OPENAI_MODEL")

client = OpenAI(api_key=api_key)
print("=" * 50)
print("AI Chatbot initialized. Type 'quit' to exit.")
print("=" * 50)
while True:
    user_input = input("\nYou: ")
    
    if(user_input.strip() == ""):
        print("Please enter a valid input.")
        continue

    if user_input.lower() == "quit":
        print("Goodbye!")
        break
    
    reponse = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL"),
        messages=[
            {
            "role": "user", 
            "content": user_input
            }
        ]
    )
    #display the response
    print("\nAI: " + reponse.choices[0].message.content)
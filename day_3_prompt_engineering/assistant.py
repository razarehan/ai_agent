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
conversations = []

roles = {
    "1": "You are a friendly school teacher. Explain every concept using simple language and real-life examples.",

    "2": "You are a senior Python developer. Explain programming concepts clearly and always include Python examples.",

    "3": "You are an experienced travel guide. Recommend places, food, transportation and travel tips.",

    "4": "You are a motivational coach. Encourage the user and give practical advice with a positive attitude.",

    "5": "You are a professional interviewer. Ask one interview question at a time and provide feedback after each answer."
}


print("\nChoose Your Assistant\n")

print("1. Teacher")
print("2. Python Expert")
print("3. Travel Guide")
print("4. Motivational Coach")
print("5. Interviewer")

choice = input("\nEnter your choice : ")

conversations = [
    {
        "role": "system",
        "content": roles.get(
            choice,
            "You are a helpful AI assistant."
        )
    }
]

while True:
    user_input = input("\nYou: ")
    
    if(user_input.strip() == ""):
        print("Please enter a valid input.")
        continue

    if user_input.lower() == "quit":
        print("Goodbye!")
        break
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
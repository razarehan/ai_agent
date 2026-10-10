import os
from dotenv import load_dotenv
from openai import OpenAI
from tools import read_file

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

    if user_input.lower().startswith("summarize") or user_input.lower().startswith("explain"):
        # user_input = "summarize <file_path>" or "explain <file_path>"
        file_path = "data/" + user_input.split(" ", 1)[1].strip()

        file_content =  read_file(file_path)

        if file_content is None:
            print("File not found.")
            continue

        user_input = user_input.split(" ", 1)[0].strip() + " the following content:\n\n" + file_content

    if user_input.lower().startswith("ask"):
        # user_input = "ask <file_path> <question>"
        file_path = "data/" + user_input.split(" ", 2)[1].strip()
        print(file_path)
        question = user_input.split(" ", 2)[2].strip()
        file_content =  read_file(file_path)

        if file_content is None:
            print("File not found.")
            continue

        user_input = f"""
            You are given a document and a question. 
            Your task is to provide a concise and accurate answer to the question based on the content of the document only.
            If the answer is not present in the document, respond with "The answer is not available in the provided document."
            Question: {question}
            Content: {file_content}
        """

    messages = [{
        "role": "user",
        "content": user_input
    }]

    response = client.chat.completions.create(
        model=os.getenv("OPENAI_MODEL"),
        messages=messages
    )

    #display the response
    print("\nAI: " + response.choices[0].message.content)
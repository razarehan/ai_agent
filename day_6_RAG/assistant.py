import os
from dotenv import load_dotenv
from openai import OpenAI
from embedding import create_embedding, cosine_similarity
from retriever import load_documents

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
model = os.getenv("OPENAI_MODEL")
embedding_model = os.getenv("OPENAI_EMBEDDING_MODEL")
client = OpenAI(api_key=api_key)

messages = []
messages.append({
    "role": "system",
    "content": "Answer only from the provided context."
})

documents = load_documents()
documents_embeddings = {}

for doc_name, content in documents.items():
    embedding = create_embedding(client, embedding_model, content)
    documents_embeddings[doc_name] = embedding

print("=" * 50)
print("AI Chatbot initialized. Type 'quit' to exit.")
print("=" * 50)

while True:
    user_input = input("\nYou: ")
    
    if(user_input.strip() == ""):
        print("Please enter a valid question.")
        continue

    if user_input.lower() == "quit":
        print("Goodbye!")
        break
    # convert user question to embedding vector
    question_embedding = create_embedding(client, embedding_model, user_input)

    # get the context from the vector database based on the user question
    best_doc_name = None
    best_score = -1
    context = None

    for doc_name, embedding in documents_embeddings.items():
        score = cosine_similarity(question_embedding, embedding)
        if score > best_score:
            best_score = score
            best_doc_name = doc_name

    if best_doc_name:
        context = documents[best_doc_name]
    
    print(f"\nRetrieved Document: {best_doc_name}")
    # create a prompt for the AI model
    prompt = f"""
    You are given a document and a question.
    Your task is to provide a concise and accurate answer to the question based on the content of the document only.
    If the answer is not present in the document, respond with "The answer is not available in the provided document."
    Question: {user_input}
    Context: {context}
    """

    messages.append({
        "role": "user",
        "content": prompt
    })
    response = client.chat.completions.create(
        model=model,
        messages=messages
    )

    #display the response
    print("\nAI: " + response.choices[0].message.content)
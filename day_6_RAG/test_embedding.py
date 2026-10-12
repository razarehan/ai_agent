import os
from dotenv import load_dotenv
from openai import OpenAI
from day_6_RAG.embedding import cosine_similarity

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
embedding_model = os.getenv("OPENAI_EMBEDDING_MODEL")

client = OpenAI(api_key=api_key)

sentence1 = client.embeddings.create(
    model=embedding_model,
    input="I want to learn Python."
)
sentence2 = client.embeddings.create(
    model=embedding_model,
    input="I want to make grip on Python."
)

vector1 = sentence1.data[0].embedding
vector2 = sentence2.data[0].embedding

similarity = cosine_similarity(vector1, vector2)

print(f"Cosine similarity between the two sentences: {similarity}")
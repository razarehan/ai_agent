import numpy as np

def cosine_similarity(vec1, vec2):
    """
    Calculate the cosine similarity between two vectors.
    
    Args:
        vec1 (list or np.ndarray): First vector.
        vec2 (list or np.ndarray): Second vector.
        
    Returns:
        float: Cosine similarity between vec1 and vec2.
    """
    # Convert lists to numpy arrays if they are not already
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    
    # Calculate the dot product and norms
    dot_product = np.dot(vec1, vec2)
    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)
    
    # Avoid division by zero
    if norm_vec1 == 0 or norm_vec2 == 0:
        return 0.0
    
    # Calculate cosine similarity
    similarity = dot_product / (norm_vec1 * norm_vec2)
    
    return similarity

def create_embedding(client, model , text):
    """
    Create an embedding for the given text using the specified model.
    
    Args:
        client (OpenAI): OpenAI client instance.
        model (str): The embedding model to use.
        text (str): The text to create an embedding for.

    Returns:
        list: The embedding vector for the given text.
    """
    response = client.embeddings.create(
        model=model,
        input=text
    )
    return response.data[0].embedding
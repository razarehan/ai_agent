from pathlib import Path

def load_documents():
    """
    Load documents from text files in the 'knowledge' directory.
    Args: 
        None
    Returns:
        dict: A dictionary of documents loaded from the file.
    """
    documents = {}
    path = Path("knowledge")
    for file in path.glob("*.txt"):
        with open(file, "r", encoding="utf-8") as f:
            documents[file.name] = f.read()
    return documents

def retriever(question):
    """
    Retrieve relevant documents based on the question.
    Args:
        question (str): The question to retrieve documents for.
    Returns:
        tuple: A tuple containing the document name and content, or (None, None) if no relevant document is found.
    """
    documents = load_documents()
    for doc_name, content in documents.items():
        if question.lower() in content.lower():
            return doc_name, content
    return None, None
from retriever import load_documents, retriever

def test_load_documents():
    """
    Test the load_documents function.
    """
    documents = load_documents()
    assert isinstance(documents, dict), "The returned value should be a dictionary."
    assert len(documents) > 0, "The dictionary should not be empty."
    for key, value in documents.items():
        print(f"Document: {key}, Content Length: {len(value)}")
        print("-" * 50);

def test_retriever(question):
    """
    Test the retriever function with a sample question.
    """
    doc_name, content = retriever(question)
    if doc_name and content:
        print(f"Retrieved Document: {doc_name}")
        print(f"Content: {content[:200]}...")  # Print first 200 characters
    else:
        print("No relevant document found.")


test_load_documents()
test_retriever("python")
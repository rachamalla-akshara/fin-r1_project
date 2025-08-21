from transformers import pipeline

# Load a small question-answering model
qa = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

context = """
Apple Inc. is a technology company based in Cupertino, California. In 2022, it had a revenue of $394 billion
and a net income of $99.8 billion. The company designs, manufactures, and markets smartphones, personal computers,
tablets, wearables, and accessories.
"""

question = "What was Apple's revenue in 2022?"

result = qa(question=question, context=context)
print("Answer:", result["answer"])

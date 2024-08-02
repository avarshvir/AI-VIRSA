# answer.py

def get_answer(question):
    question = question.lower()
    if "your name" in question:
        return "My name is AI Assistant."
    elif "how are you" in question:
        return "I'm an AI, so I don't have feelings, but thanks for asking!"
    elif "what can you do" in question:
        return "I can listen to your questions and try to answer them."
    else:
        return "I'm sorry, I don't know the answer to that."

if __name__ == "__main__":
    test_questions = [
        "What is your name?",
        "How are you?",
        "What can you do?",
        "Tell me something."
    ]
    for question in test_questions:
        print(f"Q: {question}")
        print(f"A: {get_answer(question)}")

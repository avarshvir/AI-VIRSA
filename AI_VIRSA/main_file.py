import random
from speech_to_text_virsa import listen
from text_to_speech_virsa import speak
from answer import get_answer
from time_data_virsa import get_time_based_greeting
from task_manager_virsa import handle_task, listening
from information_virsa import information_knowledge
from data_visualization import visualize_data
import time

def get_random_personalized_greeting():
    greetings = [
        "how can I help you?",
        "I am happy to see you again.",
        "Hi Boss, what's up?",
        "How can I assist you today?",
        "What do you need help with?"
    ]
    return random.choice(greetings)

def main():
    print("AI Assistant is starting...")

    time_based_greeting = get_time_based_greeting()
    personalized_greeting = get_random_personalized_greeting()
    greeting = f"{time_based_greeting} Sir, {personalized_greeting}"

    print(greeting)
    speak(greeting)

    last_task = None

    while True:
        if not listening:
            print("Pausing listening...")
            time.sleep(1)
            continue

        print("Listening...")
        question = listen()
        if question.lower() in ["exit", "quit", "bye"]:
            speak("Goodbye!")
            break
        print(f"You said: {question}")

        if question.lower() in ["repeat", "repeat it"]:
            if last_task:
                speak("Repeating the last task.")
                handle_task(last_task)
            else:
                speak("There is no task to repeat.")
        elif any(keyword in question.lower() for keyword in ["open", "news", "play music"]):
            last_task = question
            handle_task(question)
        elif "wikipedia" in question.lower() or any(
                keyword in question.lower() for keyword in ["tell me about", "what is", "who is"]):
            search_query = question.lower().replace("wikipedia", "").replace("tell me about", "").replace("what is",
                                                                                                          "").replace(
                "who is", "").strip()
            if search_query:
                try:
                    information_knowledge(search_query)
                except Exception as e:
                    speak(f"I'm sorry, I couldn't find information about {search_query}. {str(e)}")
            else:
                speak("What would you like me to search for?")
        elif "visualization" or "visualization" in question.lower():
            dataset_name = question.lower().replace("make data visualisation of", "").strip()
            if dataset_name:
                visualize_data(dataset_name)
            else:
                speak("Please specify the dataset for visualization.")
        else:
            answer = get_answer(question)
            speak(answer)

if __name__ == "__main__":
    main()

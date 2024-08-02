#information_virsa.py

import wikipedia
from text_to_speech_virsa import speak

def information_knowledge(info_question):
    try:
        answer = wikipedia.summary(info_question, sentences=2)  # Limit to 2 sentences for brevity
        speak(answer)
    except wikipedia.exceptions.DisambiguationError as e:
        options = e.options[:5]  # Get the first 5 options
        speak(f"There are multiple results for {info_question}. Some options are: {', '.join(options)}. Please be more specific.")
    except wikipedia.exceptions.PageError:
        speak(f"I'm sorry, I couldn't find any information about {info_question}.")
    except Exception as e:
        speak(f"An error occurred while searching for {info_question}. {str(e)}")
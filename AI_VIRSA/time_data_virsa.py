# time_data_virsa.py

from datetime import datetime

def get_time_based_greeting():
    current_hour = datetime.now().hour

    if 5 <= current_hour < 12:
        return "Good Morning"
    elif 12 <= current_hour < 18:
        return "Good Afternoon"
    elif 18 <= current_hour < 22:
        return "Good Evening"
    else:
        return "Hello"

if __name__ == "__main__":
    print(get_time_based_greeting())

import datetime
strfTime = datetime.datetime.now().strftime("%H:%M:%S")
hour = datetime.datetime.now().strftime("%H")
min = datetime.datetime.now().strftime("%M")
time_responses = [
    f"Sir the time is {strfTime}",
    f"Sir time is {hour} bajke {min} minutes"
]

#greeting = ""
def greet():
    current_time = datetime.datetime.now()
    #hour = int(current_time.strftime("%H"))
    hour = datetime.datetime.now().hour

    if hour < 12:
        return "Good Morning Sir!"
    elif 12 <= hour < 17:
        return "Good Afternoon Sir!"
    else:
        return "Good Evening Sir!"

greeting_msg = greet()

print(greeting_msg)
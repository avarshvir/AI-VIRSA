import datetime
strfTime = datetime.datetime.now().strftime("%H:%M:%S")
hour = datetime.datetime.now().strftime("%H")
min = datetime.datetime.now().strftime("%M")
time_responses = [
    f"Sir the time is {strfTime}",
    f"Sir time is {hour} bajke {min} minutes"
]

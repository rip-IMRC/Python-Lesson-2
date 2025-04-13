from datetime import datetime
now=datetime.now()
formatted_time=now.strftime("%Y-%m-%d %H:%M:%S")
print("Current Date and Time: ", formatted_time)
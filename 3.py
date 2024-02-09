import datetime
currentDateTime=datetime.datetime.now()
print("The curent date and time is:")
print(currentDateTime.strftime("%d-%m-20%y and %H:%M:%S"))
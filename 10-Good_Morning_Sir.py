import time

timestamp = int(time.strftime('%H%M%S'))
hour = timestamp // 10000  # Extract the hour part from the timestamp
print(hour)

if 0 <= hour < 12:
    print("Good Morning Sir!!")
elif 12 <= hour < 16:
    print("Good Afternoon Sir!!")
elif 16 <= hour < 20:
    print("Good Evening Sir!!")
else:
    print("Good Night Sir!!")

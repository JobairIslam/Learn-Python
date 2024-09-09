import time

# Get current time in HH:MM:SS format
timestamp = time.strftime('%H:%M:%S')
print(timestamp)

# Get current hour
hour = int(time.strftime('%H'))
min=int(time.strftime('%M'))
sec=int(time.strftime('%S'))
print(f"{hour:2}:{min:2}:{sec:2}")


# Check if hour is between 15 and 18
if 15 <= hour < 18:
    print("Good evening")
if 6 <= hour < 11:
    print("Good morning")
if 12 <= hour < 14:
    print("Good dupur")

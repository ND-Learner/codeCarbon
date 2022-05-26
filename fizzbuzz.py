from codecarbon import EmissionsTracker

tracker = EmissionsTracker()
tracker.start()


for num in range(1, 1000):
    if num % 15 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz") 
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num) 

tracker.stop()
emissions: float = tracker.stop()
print(emissions)

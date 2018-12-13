import time 
import threading
import random 

def say_something(lo, hi):
    i = 0
    while True:
        number = random.randint(lo, hi)
        print(f"Random number #{i} is {number}\n")
        i += 1
        time.sleep(5)


try:
    curr = threading.Thread(target=say_something, args=(10, 100))
    curr.start()
    while True:
        user_input = input("")
        print(f"You said {user_input}")
        if user_input == '-1':
            curr._stop()
except:
    print("Error!")

    
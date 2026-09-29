import threading
import time

def take_order():
    for i in range(1, 4):
        print(f"Taking Order for #{i}")
        time.sleep(2)

def brew_chai():
    for i in range(1, 4):
        print(f"Brewing Chai for #{i}")
        time.sleep(3)

# Creating threads
order_thread = threading.Thread(target=take_order)
brew_thread = threading.Thread(target=brew_chai)

# Starting threads
order_thread.start()
brew_thread.start()

# Waiting for threads to finish
order_thread.join()
brew_thread.join()

print("All threads finished")
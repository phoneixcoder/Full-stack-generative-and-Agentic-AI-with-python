import threading
import time

def background_worker():
    while True:
        print("Background worker running")
        time.sleep(2)

t = threading.Thread(target=background_worker, daemon=True)
t.start()

print("Main Program ended")
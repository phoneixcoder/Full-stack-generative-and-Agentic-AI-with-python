import threading

counter = 0
# If global interpreter lock is not used, the counter will be shared between threads
# and the result will be unpredictable
# So we use lock to ensure that the counter is incremented atomically
lock = threading.Lock()

def increament():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1

threads = [threading.Thread(target=increament) for _ in range(10)]
[t.start() for t in threads]
[t.join() for t in threads]

print(f"Final counter: {counter}")
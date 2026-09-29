import threading
import time

def cup_heavy():
    print(f"Heating cup...")
    total = 0
    for i in range(10**7):
        total += i
    print(f"Done")

start = time.time()
threads = [threading.Thread(target=cup_heavy) for _ in range(2)]
[t.start() for t in threads]
[t.join() for t in threads]
end = time.time()

print(f"Time taken: {end - start:.2f} seconds")
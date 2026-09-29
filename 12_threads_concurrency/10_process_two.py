from multiprocessing import Process
import time

def cup_heavy():
    print(f"Heating cup...")
    total = 0
    for i in range(10**9):
        total += i
    print(f"Done")

if __name__ == "__main__":
    start = time.time()
    processes = [Process(target=cup_heavy) for _ in range(2)]
    [p.start() for p in processes]
    [p.join() for p in processes]

    end = time.time()
    print(f"Time taken: {end - start:.2f} seconds")
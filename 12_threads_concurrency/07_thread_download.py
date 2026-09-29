import threading
import requests
import time

def download(url):
    print(f"Started Downloading from {url} ...")
    resp = requests.get(url)
    print(f"Finished downloading from {url}, size: {len(resp.content)} bytes")

urls = [
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/svg",
]

start = time.time()
threads = [threading.Thread(target=download, args=(url,)) for url in urls]
for t in threads:
    t.start()
for t in threads:
    t.join()
end = time.time()
print(f"Time taken: {end - start:.2f} seconds")
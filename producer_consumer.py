# code source: https://techmonger.github.io/55/producer-consumer-python/
import threading
from threading import Thread
from queue import Queue

q = Queue()
final_results = []

def producer():
    for i in range(100):
        q.put(i)
        

thread_lock = threading.Lock()
def consumer():
    while True:
        # First addition
        thread_lock.acquire()
        number = q.get()
        result = (number, number**2)
        final_results.append(result)
        q.task_done()
        # Second addition
        thread_lock.release()
        

for i in range(5):
    t = Thread(target=consumer)
    t.daemon = True
    t.start()
   

producer()

q.join()

print (final_results)
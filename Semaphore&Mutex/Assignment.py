from threading import Semaphore, Thread
from time import sleep
CAPACITY = 10
buffer = [-1]*CAPACITY
mutex = Semaphore()
empty = Semaphore(CAPACITY)
full = Semaphore(0)
in_index = 0
out_index = 0
print(buffer)
print(mutex)


class Producer(Thread):
    def run(self):
        global CAPACITY, buffer, in_index, out_index, empty, full, mutex
        items_produced = 0
        counter = 0
        while items_produced < 20:
            empty.acquire()
            mutex.acquire()

            counter += 1
            buffer[in_index] = counter
            in_index = (in_index+1) % CAPACITY
            print("Produced: ", counter)

            mutex.release()
            full.release()
            sleep(0)
            items_produced += 1


class Consumer(Thread):
    def run(self):
        global CAPACITY, in_index, out_index, empty, full, mutex, buffer, counter
        items_consumed = 0
        while items_consumed < 20:
            full.acquire()
            mutex.acquire()

            item = buffer[out_index]
            out_index = (out_index+1) % CAPACITY
            print(f"Consumed Item: {item}")
            mutex.release()
            empty.release()
            sleep(0)
            items_consumed += 1


pro = Producer()
con = Consumer()

pro.start()
con.start()

pro.join()
con.join()

print(buffer)
print(mutex)

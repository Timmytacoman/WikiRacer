from threading import Thread
import time

i = 0


def task():
    print("start task")
    time.sleep(1)
    print("end task")


startTime = time.time()

t1 = Thread(target=task)
t2 = Thread(target=task)

t1.start()
t2.start()

t1.join()
t2.join()

endTime = time.time()
print(f"Elapsed time: {endTime - startTime}")

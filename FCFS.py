import threading
import queue
import random
import time

# Queue for customers
customer_queue = queue.Queue(maxsize=7) # Thala for a reason

# Number of tellers
num_tellers = 3
tellers = [None] * num_tellers
teller_locks = [threading.Lock() for _ in range(num_tellers)]

def customer_arrival(customer_id):
    try:
        customer_queue.put_nowait(customer_id)
        print(f"Customer{customer_id} enters the Queue")
    except queue.Full:
        print("Queue is FULL.")

def teller_service(teller_id):
    while True:
        customer_id = customer_queue.get()
        print(f"Customer {customer_id} is in Teller{teller_id}")
        service_time = random.randint(1, 5)
        time.sleep(service_time)  # Simulate service time
        print(f"Customer {customer_id} leaves the Teller{teller_id}")
        customer_queue.task_done()

# Create teller threads
for i in range(num_tellers):
    t = threading.Thread(target=teller_service, args=(i+1,))
    t.daemon = True  # Daemon threads will shut down with the main program
    t.start()

# Simulate customer arrivals
customer_id = 1
while True:
    customer_arrival(customer_id)
    customer_id += 1
    time.sleep(random.randint(1, 3))  # Random arrival time

    if input("Press any key to stop..."):
        break

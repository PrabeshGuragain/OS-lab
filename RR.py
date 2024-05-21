import time
import threading
import queue
import random

# Given
num_tellers = 3
quantum = 2  

# Other paramaters
customer_queue = queue.Queue(maxsize=7) # Thala for a reason
# Tot_waiting_time, Tot_turnaround_time = 0, 0

def customer_arrival_rr(customer_id):
    service_time = random.randint(1, 5)
    customer_queue.put((service_time, customer_id))
    print(f"Customer{customer_id} enters the Queue with service time {service_time}")

def teller_service_rr(teller_id):
    while True:
        if not customer_queue.empty():
            service_time, customer_id = customer_queue.get()
            served_time = min(quantum, service_time)
            print(f"Customer {customer_id} is in Teller{teller_id} for {served_time} seconds")
            time.sleep(served_time)
            remaining_time = service_time - served_time

            if remaining_time > 0:
                customer_queue.put((remaining_time, customer_id))
            else:
                print(f"Customer {customer_id} leaves the Teller{teller_id}")

# Create teller threads
for i in range(num_tellers):
    t = threading.Thread(target=teller_service_rr, args=(i+1,))
    t.daemon = True
    t.start()

# Simulate customer arrivals for calculating average times
for i in range(20):  # for example, 20 customers
    customer_arrival_rr(i+1)
    time.sleep(random.randint(1, 3))  # customers arrive at random intervals
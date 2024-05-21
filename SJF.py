import heapq
import threading
import random 
import time

# Priority Queue for customers based on service time
num_tellers  = 3 # Given
customer_queue = []
queue_lock = threading.Lock()

def customer_arrival_sjf(customer_id):
    service_time = random.randint(1, 5)
    with queue_lock:
        heapq.heappush(customer_queue, (service_time, customer_id))
    print(f"Customer{customer_id} enters the Queue with service time {service_time}")

def teller_service_sjf(teller_id):
    while True:
        with queue_lock:
            if customer_queue:
                service_time, customer_id = heapq.heappop(customer_queue)
            else:
                continue

        print(f"Customer {customer_id} is in Teller{teller_id} for {service_time} seconds")
        time.sleep(service_time)
        print(f"Customer {customer_id} leaves the Teller{teller_id}")

# Create teller threads
for i in range(num_tellers):
    t = threading.Thread(target=teller_service_sjf, args=(i+1,))
    t.daemon = True
    t.start()

# Simulate customer arrivals
customer_id = 1
while True:
    customer_arrival_sjf(customer_id)
    customer_id += 1
    time.sleep(random.randint(1, 3))

    if input("Press any key to stop..."):
        break

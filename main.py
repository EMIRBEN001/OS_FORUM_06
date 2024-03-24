# this is my attempt at the multitreading program using python

import threading
import random

LOWER_NUM = 1
UPPER_NUM = 10000
BUFFER_SIZE = 100
MAX_COUNT = 10000

# this function is to check if the number is even or not, by returning true or false
def is_even(number):
    return number % 2 == 0

# this is the Producer thread
def producer(buffer, max_count):
    with open("all.txt", "w") as f:
        for _ in range(max_count):
            number = random.randint(LOWER_NUM, UPPER_NUM)
            f.write(str(number) + "\n")

# and this is the Customer thread to handle even numbers
def even_customer(buffer, max_count):
    count = 0
    with open("all.txt", "r") as f:
        while count < max_count:
            with threading.Lock():
                line = f.readline().strip()
                if not line:
                    break
                number = int(line)
                if is_even(number):
                    with open("even.txt", "a") as even_file:
                        even_file.write(str(number) + "\n")
                    count += 1

# same thing but for the odd numbers (Customer Thread)
def odd_customer(buffer, max_count):
    count = 0
    with open("all.txt", "r") as f:
        while count < max_count:
            with threading.Lock():
                line = f.readline().strip()
                if not line:
                    break
                number = int(line)
                if not is_even(number):
                    with open("odd.txt", "a") as odd_file:
                        odd_file.write(str(number) + "\n")
                    count += 1

# Creating the buffer
buffer = []

# Creating the threads
producer_thread = threading.Thread(target=producer, args=(buffer, MAX_COUNT))
even_customer_thread = threading.Thread(target=even_customer, args=(buffer, MAX_COUNT))
odd_customer_thread = threading.Thread(target=odd_customer, args=(buffer, MAX_COUNT))

# Starting the threads
producer_thread.start()
even_customer_thread.start()
odd_customer_thread.start()

# Waiting for threads to finish
producer_thread.join()
even_customer_thread.join()
odd_customer_thread.join()

print("Program terminated.") # it indicates the program is done so that there will be no error where the consumer is going beyond the expected value

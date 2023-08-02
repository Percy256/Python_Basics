# import multiprocessing
# def process_task(name):
#     print(f"Processing task {name}")


# #Create a pool of processes
# pool= multiprocessing.Pool(processes=5)

# #Submit multiple task to the pool
# for i in range(6):
#     pool.apply_async(process_task, args=(f"Process {i}",))

# #Close the pool and wait for all processes to finish
# pool.close()
# pool.join()



"""
#Example of multiprocessing

# import multiprocessing
# def process_task(name):
#     print(f"Processing task {name}")

# #Create a pool of processes
# pool= multiprocessing.Pool(processes=5)

# #Submit multiple task to the pool
# for i in range(6):
#     pool.apply_async(process_task, args=(f"Process {i}",))

# #Close the pool and wait for all processes to finish
# pool.close()
# pool.join()


"""
import time
import threading
from multiprocessing import Process

# Function to be executed
def run_function(duration):
    print(f"Function started for {duration} seconds")
    time.sleep(duration)
    print(f"Function finished for {duration} seconds")

# Multithreading example
def run_multithreading():
    durations = [1, 2, 3]  # Different durations for the function

    # Create and start threads for each duration
    threads = []
    for duration in durations:
        t = threading.Thread(target=run_function, args=(duration,))
        threads.append(t)
        t.start()

    # Wait for all threads to complete
    for t in threads:
        t.join()

    print("Multithreading finished")

# Multiprocessing example
def run_multiprocessing():
    durations = [1, 2, 3]  # Different durations for the function

    # Create and start processes for each duration
    processes = []
    for duration in durations:
        p = Process(target=run_function, args=(duration,))
        processes.append(p)
        p.start()

    # Wait for all processes to complete
    for p in processes:
        p.join()

    print("Multiprocessing finished")

# Run the examples
run_multithreading()
run_multiprocessing()

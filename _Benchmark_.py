import time
import numpy as np
import multiprocessing

def basic_operations():
    """ Measures basic arithmetic operations per second. """
    x = 0
    start = time.time()
    while time.time() - start < 1:  # Run for 1 second
        x += 1
    return x

def loop_operations():
    """ Measures loop iterations per second. """
    count = 0
    start = time.time()
    while time.time() - start < 1:
        count += 1
    return count

def numpy_operations():
    """ Measures NumPy vectorized operations per second. """
    arr = np.random.rand(1000000)
    start = time.time()
    for _ in range(100):  # Run multiple times
        arr += 1
    elapsed = time.time() - start
    return (100 * len(arr)) / elapsed  # Operations per second

def parallel_task(_):
    """ Task for multiprocessing test. """
    x = 0
    for _ in range(1000000):
        x += 1
    return x

def multiprocessing_operations():
    """ Measures multiprocessing performance. """
    num_cores = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=num_cores)
    start = time.time()
    pool.map(parallel_task, range(num_cores))
    elapsed = time.time() - start
    return num_cores * (1000000 / elapsed)  # Estimated operations per second

# Run benchmarks
print("Benchmarking...")

basic_ops = basic_operations()
loop_ops = loop_operations()
numpy_ops = numpy_operations()
multi_ops = multiprocessing_operations()

print(f"Basic Arithmetic Operations/sec: {basic_ops:,}")
print(f"Loop Iterations/sec: {loop_ops:,}")
print(f"NumPy Vectorized Operations/sec: {numpy_ops:,.0f}")
print(f"Multiprocessing Operations/sec: {multi_ops:,.0f}")

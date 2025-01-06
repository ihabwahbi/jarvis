import time
import multiprocessing
import numpy as np
import psutil


def cpu_intensive_task(_=None):
    # Increase workload for better measurement
    size = 2000  # Larger matrix
    A = np.random.rand(size, size)
    B = np.random.rand(size, size)
    start = time.time()
    for _ in range(10):  # More iterations
        np.dot(A, B)
    return time.time() - start


def benchmark_cpu():
    # System info
    print("\nSystem Information:")
    print(f"CPU Cores: {multiprocessing.cpu_count()}")
    print(f"Memory: {psutil.virtual_memory().total / (1024**3):.1f} GB")

    # CPU usage and memory details
    print("\nCurrent Resource Usage:")
    print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")
    print(f"Memory Usage: {psutil.virtual_memory().percent}%")

    # Single-core performance
    print("\nSingle-core benchmark:")
    single_core_time = cpu_intensive_task()
    print(f"Time taken: {single_core_time:.2f} seconds")

    # Multi-core performance using multiprocessing
    print("\nMulti-core benchmark:")
    with multiprocessing.Pool() as pool:
        start = time.time()
        results = pool.map(cpu_intensive_task, range(multiprocessing.cpu_count()))
        total_time = time.time() - start
        print(f"Total time taken: {total_time:.2f} seconds")
        print(f"Average time per core: {sum(results)/len(results):.2f} seconds")
        theoretical_speedup = (
            single_core_time * multiprocessing.cpu_count() / total_time
        )
        print(f"Parallel efficiency: {theoretical_speedup:.2f}x speedup")


if __name__ == "__main__":
    benchmark_cpu()

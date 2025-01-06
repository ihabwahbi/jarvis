import os
import time


def benchmark_disk():
    # File size in MB
    size = 1000

    print(f"Writing {size}MB file...")
    start = time.time()
    with open("test_file", "wb") as f:
        f.write(os.urandom(size * 1024 * 1024))
    write_time = time.time() - start
    print(f"Write speed: {size/write_time:.1f} MB/s")

    print("\nReading file...")
    start = time.time()
    with open("test_file", "rb") as f:
        f.read()
    read_time = time.time() - start
    print(f"Read speed: {size/read_time:.1f} MB/s")

    # Cleanup
    os.remove("test_file")


if __name__ == "__main__":
    benchmark_disk()

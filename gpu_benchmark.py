import time
import torch


def benchmark_gpu():
    print(f"CUDA Available: {torch.cuda.is_available()}")
    print(f"GPU Device: {torch.cuda.get_device_name(0)}")
    print(f"CUDA Version: {torch.cuda.get_device_capability(0)}")
    print(f"PyTorch Version: {torch.__version__}")

    # Memory test
    print("\nMemory Test:")
    print(
        f"Total GPU Memory: {torch.cuda.get_device_properties(0).total_memory / 1024**3:.2f} GB"
    )
    print(f"Initially Allocated: {torch.cuda.memory_allocated() / 1024**3:.2f} GB")
    print(f"Initially Cached: {torch.cuda.memory_reserved() / 1024**3:.2f} GB")

    # Performance tests
    sizes = [(1000, 1000), (2000, 2000), (4000, 4000), (8000, 8000)]

    for size in sizes:
        print(f"\nBenchmarking matrix multiplication {size[0]}x{size[1]}")

        # GPU computation
        torch.cuda.synchronize()
        a_gpu = torch.randn(*size, device="cuda")
        b_gpu = torch.randn(*size, device="cuda")

        # Warmup
        torch.matmul(a_gpu, b_gpu)
        torch.cuda.synchronize()

        # Benchmark
        start = time.time()
        for _ in range(10):
            torch.matmul(a_gpu, b_gpu)
            torch.cuda.synchronize()
        gpu_time = (time.time() - start) / 10

        print(f"Average time per operation: {gpu_time*1000:.2f} ms")
        print(f"Memory Used: {torch.cuda.memory_allocated() / 1024**3:.2f} GB")


if __name__ == "__main__":
    benchmark_gpu()

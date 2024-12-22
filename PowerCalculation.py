import time
import sys
sys.setrecursionlimit(10000)  # Tingkatkan batas rekursi menjadi 10.000


def power_iterative(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result

def power_recursive(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power_recursive(base, exponent - 1)

# Fungsi untuk mencatat waktu eksekusi
def measure_time(func, base, exponent):
    start_time = time.time()
    result = func(base, exponent)
    end_time = time.time()
    elapsed_time_ms = (end_time - start_time) * 1000  # Konversi ke milidetik
    return result, elapsed_time_ms

# Data pengujian
inputs = [10, 100, 1000, 5000]
base = 2

print("--- Iterative Results ---")
for exponent in inputs:
    try:
        result, elapsed_time_ms = measure_time(power_iterative, base, exponent)
        print(f"Base: {base}, Exponent: {exponent}, Time: {elapsed_time_ms:.3f} ms")
    except Exception as e:
        print(f"Base: {base}, Exponent: {exponent}, Error: {str(e)}")

print("\n--- Recursive Results ---")
for exponent in inputs:
    try:
        result, elapsed_time_ms = measure_time(power_recursive, base, exponent)
        print(f"Base: {base}, Exponent: {exponent}, Time: {elapsed_time_ms:.3f} ms")
    except RecursionError:
        print(f"Base: {base}, Exponent: {exponent}, Error: Recursion limit reached")

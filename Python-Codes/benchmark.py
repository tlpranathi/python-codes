import timeit

# number of iterations for testing
iterations = 1_000_000
n = 500  # sample value within the range

# test 1: Using direct comparison
time_direct = timeit.timeit('1 <= n <= 1000', globals = globals(), number = iterations)

# test 2: Using range
time_range = timeit.timeit('n in range(1, 1001)', globals = globals(), number = iterations)

# results
print(f"Direct comparison: {time_direct:.6f} seconds")
print(f"Range check:       {time_range:.6f} seconds")

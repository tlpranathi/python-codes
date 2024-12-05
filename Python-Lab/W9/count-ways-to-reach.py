def count_ways_to_reach(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    return count_ways_to_reach(n-1) + count_ways_to_reach(n-2)+ count_ways_to_reach(n-3)

print(count_ways_to_reach(n = int(input("Enter number: "))))

def is_power_of_4(n):
    if n == 1:
        return 'T'
    elif n % 4 != 0:
        return 'F'
    return is_power_of_4(n/4)

print(is_power_of_4(n = int(input("Enter number: "))))
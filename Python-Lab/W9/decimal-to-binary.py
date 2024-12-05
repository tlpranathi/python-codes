def decimal_to_binary(n):
    if n == 0:
        return ""
    return str(decimal_to_binary(n // 2)) + str(n % 2) 

print(decimal_to_binary(n = int(input("Enter number: "))))
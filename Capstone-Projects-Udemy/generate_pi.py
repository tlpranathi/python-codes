# find pi to the nth digit
from mpmath import mp # or decimal

def generate_pi(n):
        mp.dps = n  # set the number of decimal places
        return str(mp.pi)

while True:
    try:
        n = int(input("Enter a number between 1 and 1000: "))
        
        if 1 <= n <= 1000:
            print(f"\npi to {n} places is:\n{generate_pi(n+1)}")
            break
        else:
            print("\nEnter a number between 1 and 1000!!!\n")
    
    except ValueError:
         print("\nInvalid input. Enter a number within range!!!\n")
    
    

# math.pi module can only be precise to about 15-16 decimal places 

# from math import pi

# def generate_pi(n):
#     if n in range(1, 1001):
#         return f"{pi:.{n}f}"s
#     else:
#         return "enter number between 1 and 1000"

# n = int(input("enter number between 1 and 1000: "))
# print("pi to", n, "places is:", generate_pi(n))

from mpmath import mp # or decimal

def generate_e(n):
        mp.dps = n  # set the number of decimal places
        return str(mp.e)

while True:
    try:
        n = int(input("Enter a number between 1 and 1000: "))
        
        if 1 <= n <= 1000:
            print(f"\ne to {n} places is:\n{generate_e(n+1)}")
            break
        else:
            print("\nEnter a number between 1 and 1000!!!\n")
    
    except ValueError:
         print("\nInvalid input. Enter a number within range!!!\n")
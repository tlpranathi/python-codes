string = input("enter string to be reversed: ") 
n = len(string) 
for i in range(n): 
    m = (n - 1) - i 
    print(list(string)[m], end = "")
    
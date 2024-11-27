n = int(input("number of items: ")) 
lst = [ ] 

for i in range(n): 
    ele = int(input(f"enter item {i+1}: ")) 
    lst.append(ele) 

e = [ ] 
o = [ ] 

for j in lst: 
    if j % 2 == 0: 
        e.append(j) 
    else: 
        o.append(j) 

print("even numbers:", e)
print("odd numbers:", o)
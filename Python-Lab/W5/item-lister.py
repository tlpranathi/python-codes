n = int(input("number of items: ")) 
lst = [ ] 

for i in range(n): 
    ele = input(f"enter item {i+1}: ") 
    lst.append(ele) 

for j in lst: 
    print(j) 
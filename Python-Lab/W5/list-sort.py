n = int(input("number of items: ")) 
lst = [ ] 

for i in range(n): 
    ele = int(input(f"enter item {i+1}: ")) 
    lst.append(ele) 
print("entered list: ", lst) 

if lst == sorted(lst): 
    print("entered list is already sorted") 
else: 
    lst.sort() 
    print("entered list isn't sorted, the sorted list is:", lst)
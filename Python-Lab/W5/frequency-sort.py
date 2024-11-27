num = int(input("enter number of items: ")) 
list1 = [] 

for i in range(num): 
    item1 = int(input(f"enter item {i+1}: ")) 
    list1.append(item1) 

counts = {} 

for j in list1: 
    counts[j] = list1.count(j) 
    least = min(counts.values()) 
print("the frequency of least frequent element is", least) 

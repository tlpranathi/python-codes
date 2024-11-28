lst = [1,2,4,4,2,7,8,0,7,8,8,8,-1,-1,-1]
print("initial list:", lst)

counts = {lst[i]:lst.count(i) for i in lst}
keys = list(counts.keys())
keys.sort()

lst2 = []
for i in keys:
    for j in range(counts[i]):
        lst2.append(i)

print("sorted list:", lst2)
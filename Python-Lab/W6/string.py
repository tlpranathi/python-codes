string = input("enter string: ").replace(" ", "")
count = {}
for i in string:
    count[i] = count.get(i, 0) + 1
for j in string:
    if count[j] == 1:
        print("the first non repeating character is:", i)
        break
else:
        print("there is no non repeating character in the string entered")
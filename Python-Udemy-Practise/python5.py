# UDEMY PYTHON COURSE

# ADVANCED NUMBERS
print(hex(13))
print(bin(512))

print(pow(2, 4))   # 2 to the power 4
# pow(x,y,z) >>>>>>> (x**y) % z

print(abs(-345678))
print(round(2.8345678, 3))

# ADVANCED STRINGS
s = "python programming"
print(s.capitalize())
print(s.lower())
print(s.upper())
print(s.count("n"))
print(s.find("p"))

print(s.center(50,"x"))
print("python\tprogramming")  # \t >>> escape character for tab
print("help\thelp".expandtabs())
# check rest in class 12 textbook

# ADVANCED SETS
p = set()
p.add(1)
p.add(2)
print(p)
p.clear()
p = {1, 2, 3}
pc = p.copy()
print(pc)
p.add(4)

print(p.difference(pc))
p.difference_update(pc)
print(p)

q = {1, 2, 3, 4}
q.discard(3)
print(q)

print(q.intersection(p))
q.intersection_update(p)
print(q)

# check isdisjoint
# issubset
# issuperset
# s1.symmetric_differnec(s2)
# s1.union(s2)
# s1.update(s2)

# ADVANCED DICTIONARIES
d = {"k1":1, "k2":2}
print({k:v**2 for k, v in zip(["a", "b"], range(2))})

print(d.values())

# ADVANCED LISTS
# check class 12 textbook


from datetime import datetime

def time_difference(time):
    time_format = "%H:%M:%S"

    t1 = datetime.strptime(time, time_format)
    now = datetime.now()
    current_time = now.strftime(time_format)
    t2 = datetime.strptime(current_time, time_format)
    time_diff = t2 - t1

    return time_diff


time = input("Enter time (HH:MM:SS): ")

difference = time_difference(time)
print("Difference between given time and current time is:", difference)


# MY ANSWER (NOT EFFICIENT)

num1 = int(input("number 1: "))
num2 = int(input("number 2: "))

if num1 < 0 <= num2:
    for i in range(num1, -1):
        print(i + 1, end = " ")

elif num2 < 0 <= num1:
    for i in range(num2, -1):
        print(i + 1, end = " ")

elif num1 < num2 < 0:
    if num1 + 1 == num2 or num1 - 1 == num2:
        print("no negative numbers")
    else:
        for i in range(num1, num2 - 1):
            print(i + 1, end=" ")

elif num2 < num1 < 0:
    if num1 + 1 == num2 or num1 - 1 == num2:
        print("no negative numbers")
    else:
        for i in range(num2, num1 - 1):
            print(i + 1, end=" ")

else:
    print("no negative numbers")



# MUCH BETTER CODE

if num1 > num2:
    num1, num2 = num2, num1

negative_numbers = [i + 1 for i in range(num1, num2 - 1) if i + 1 < 0]

if negative_numbers:
    print("Negative numbers between", num1, "and", num2, "are:")
    for num in negative_numbers:
        print(num, end=" ")
else:
    print("No negative numbers between", num1, "and", num2)




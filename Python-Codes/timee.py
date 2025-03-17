import time
print(time.gmtime(0))

curr = time.time()
print("Current time in seconds since epoch =", curr)

now = time.ctime(curr)
print("Current time:", now) 

for i in range(4):
    time.sleep(0.5)
    print(i)
event1 = {"a", "b", "c", "d", "e", "f", "g", "h"}
print("event 1:", event1)

event2 = {"a", "b", "w", "x", "y", "z"}
print("event 2:", event2)

print("students who attended both events:", event1 & event2)
print("students who attended only 1 event:", (event1.union(event2) - (event1&event2)))
print("students who attended atleast 1 event:", event1.union(event2))

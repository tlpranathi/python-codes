s =[("890", "ram", (95,78,99)), ("123", "kishan", (90,98,89)), ("567", "arjun", (59,68,100))]
def sort(s, callback):
    result = sorted(s, key = callback) # key >>> a function to execute to decide the order, default is None
    print(result)

def sort_name(s):
    return s[1]

def sort_marks(s):
    return -(s[2][0] + s[2][1] + s[2][2]) # descending order

print("sorting list based on names:")
sort(s, sort_name)
print("\nsorting list based on pcm total:")
sort(s, sort_marks)


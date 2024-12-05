def flatten_list(l):
    out = []
    for i in l:
        if str(type(i)) == "<class 'int'>": # or use isinstance
            out.append(i)
        elif str(type(i))!= "<class 'int'>":  
            out.extend(flatten_list(i))  
    return out

print(flatten_list([1, [2, [3, 4]], [5, 6]]))


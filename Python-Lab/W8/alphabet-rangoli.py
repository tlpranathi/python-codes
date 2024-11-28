def rangoli(size):
    al = "abcdefghijklmnopqrstuvwxyz"
    rows = []
    for i in range(size):
        s = "-".join(al[size-1:i:-1] + al[i:size])
        rows.append(s.center(4*size - 3, "-"))
    print("\n".join(rows[:0:-1] + rows))
n = int(input())
rangoli(n)
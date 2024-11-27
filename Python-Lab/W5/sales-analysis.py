sales = [12300, 34029, 28282, 27383, 81737, -18939, 18388, 72838, 12300, 34029, 28282, 27383, 81737, -18939, 18388, 72838, 12300, 34029, 28282, 27383, 81737, -18939, 18388, 72838, 12300, 34029, 28282, 27383, 81737, -18939]
sum = 0

for i in sales:
    if i < 0:
        sales.remove(i)
    sum += i

lst1 = [i for i, value in enumerate(sales) if value == max(sales)]
lst2 = [i for i, value in enumerate(sales) if value == min(sales)]
avg = sum/(len(sales))

print("average sales of the month:", avg)

print("highest sales on the day(s):")
for i in lst1:
    print(i+1,end = " ")

print("\nlowest sales on the day(s):")
for i in lst2:
    print(i+1, end =" ")


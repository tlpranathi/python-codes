p1 = {"a":10, "b":20, "c":30}
p2 = {"a":10, "d":40}
p3 = {"d":40, "e":50, "f":60}

p4 = p1|p2|p3
each_item_cost = p4

obj = []
for i, j in p4.items():
    obj.append(i)

p5 = (p1.keys() & p2.keys())|(p2.keys()&p3.keys())|(p3.keys()&p1.keys())
common_items = p5

member_totals = [sum(p1.values()), sum(p2.values()), sum(p3.values())]

total = 0
for k in p4.values():
    total += k
final_cost = total

result = {"each_item_cost":each_item_cost,"common_items":common_items,"member_totals":member_totals, "final_cost":final_cost}
print(result)

attendance_records = [("A", "P"), ("B", "A"), ("C", "P"), ("D", "A"), ("E", "P"), 
("F", "P"), ("G", "A"), ("H", "P"), ("I", "P"), ("J", "P")] 

p = 0 
a = 0 

for i in attendance_records: 
    if i[1] == "P": 
        p += 1 
    else: 
        a += 1 

print("number of students present:", p) 
print("number of students absent:", a) 

name = input("enter name: ") 
attendance = input("enter P or A: ") 

updated_records = [] 

for i, j in attendance_records: 
    if i == name and j != attendance: 
        updated_records.append((i, attendance)) 
    else: 
        updated_records.append((i, j)) 
attendance_records = updated_records 
print(attendance_records) 

name = input("enter name: ") 
attendance = input("enter P or A: ") 

attendance_records.append((name, attendance)) 
print(attendance_records) 
student = {"a":90, "b":94, "c":87, "d":73, "e":50, "f":39}

scores = [marks for marks in student.values()]
max_marks = max(scores)

topper = [name for name, marks in student.items() if marks == max_marks]
print("student marks:", student)
print("student with highest marks:", topper[0], "-", max_marks)

average_marks = sum(scores)/len(scores)
print("class average is:", average_marks)

student["g"] = 80
print("updated student marks:", student)
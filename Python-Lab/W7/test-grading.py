with open("output_key.txt", "r") as key_file:
    key_lines = key_file.readlines()
    check = [key.split(":")[1].strip() for key in key_lines]
        
n = 10
for i in range(1, n+1):
    with open(f"student_{i}.txt", "r") as f:
        lines = f.readlines()
        marks = 0
        answer = [line.split(":")[1].strip() for line in lines]
        for j in range(len(check)):
            if answer[j] == check[j]:
                marks += 2
    print(f"Marks of student {i}:", marks) 

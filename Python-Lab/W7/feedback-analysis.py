import csv

keywords = ["services", "price", "quality"]
good_feedback = ["excellent", "good", "satisfied", "happy", "good"]
bad_feedback = ["poor", "bad", "disappointed", "unsatisfied", "problem"]
good_feedback_count = 0
bad_feedback_count = 0
keyword_counts = {keyword: 0 for keyword in keywords}

with open("good_feedback.txt", mode="a") as good_file, open("bad_feedback.txt", mode="a") as bad_file,  open("feedback.txt", mode="r") as feedback_file:
    
    read_all_feedback = feedback_file.readlines()
    for each_line in read_all_feedback:
        feedback = each_line.lower()
        
        for keyword in keywords:
            keyword_counts[keyword] += feedback.count(keyword)
            
        if any(word in feedback for word in good_feedback):
            good_file.write(each_line)
            good_feedback_count += 1
        elif any(word in feedback for word in bad_feedback):
            bad_file.write(each_line)
            bad_feedback_count += 1

with open("keyword_counts.csv", mode="a", newline="") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["keyword", "count"])
    for keyword, count in keyword_counts.items():
        writer.writerow([keyword, count])
    writer.writerow([])
    writer.writerow(["Good feedback count", good_feedback_count])
    writer.writerow(["Bad feedback count", bad_feedback_count])

print("Keyword counts:")
for keyword, count in keyword_counts.items():
    print(f"{keyword}: {count}")
print(f"Good feedback count: {good_feedback_count}")
print(f"Bad feedback count: {bad_feedback_count}")
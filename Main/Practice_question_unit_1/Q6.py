import csv

STUDENT_DATA = "../../Data/students.csv"
OUTPUT_FILE = "../../Outputs/total_students.csv"

total = {}
with open(STUDENT_DATA, "r", encoding="utf-8") as f:
   reader = csv.DictReader(f)
   for row in reader:
      total[row['Name']] = int(row['Science']) + int(row['English']) + int(row['Maths'])

with open(OUTPUT_FILE, "w", encoding="utf-8", newline='') as f:
   writer = csv.DictWriter(f, fieldnames=["Name", "Total"])
   writer.writeheader()
   for name, total_marks in total.items():
      writer.writerow({"Name": name, "Total": total_marks})
      
# print(total)
      
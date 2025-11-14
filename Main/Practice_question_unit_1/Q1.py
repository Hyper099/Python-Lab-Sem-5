import csv

INPUT_FILE = "../../Data/students.csv"

with open(INPUT_FILE, "r") as f:
   reader = csv.DictReader(f)
   for row in reader:
      print(row)
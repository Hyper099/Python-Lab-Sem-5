import csv

DATA = "../../Data/employee.csv"
fieldnames = ["Name", "Department", "Salary"]

with open(DATA, "w", newline='', encoding='utf-8') as f:
   writer = csv.DictWriter(f, fieldnames=fieldnames)
   writer.writeheader()
   
   for i in range(1,6):
      name = str(input(f"Enter Name {i}: "))
      dept = str(input(f"Enter department {i}: "))
      sal = str(input(f"Enter Salary {i}: "))
      writer.writerow({
         "Name": name,
         "Department": dept,
         "Salary": sal
      })
   
   print("Done")
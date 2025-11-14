import csv


tot = {}
with open("./Practice_question_unit_1/sales.csv", "r", encoding="utf-8") as f:
   reader = csv.DictReader(f)
   # print(reader.fieldnames)
   for row in reader:
      p = row["Product"]
      q = int(row['Quantity'])
      pr = float(row["Price"])
      
      tot[p] = {
         "Price" : q*pr
      }

with open("./Practice_question_unit_1/sales_sum.csv", "w",encoding="utf-8") as f:
   writer = csv.DictWriter(f, fieldnames=["Product", "Price"])
   writer.writeheader()
   
   for key, values in tot.items():
      writer.writerow({
         "Product": key,
         "Price": values["Price"]
      })
   
      
      
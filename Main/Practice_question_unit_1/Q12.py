import csv
import os
import pathlib
import pandas as pd

INPUT_DIR= "./Practice_question_unit_1/sales_data"
os.makedirs(INPUT_DIR, exist_ok=True)

combined = []
head = False
for file in os.listdir(INPUT_DIR):
   if file.endswith(".csv"):
      with open(pathlib.Path(INPUT_DIR, file), "r", encoding="utf-8") as f:
         reader = csv.DictReader(f)
         for row in reader:
            combined.append(row)
            
print(len(combined))


df_list = []
for file in os.listdir(INPUT_DIR):
   if file.endswith(".csv"):
      df_list.append(pd.read_csv(pathlib.Path(INPUT_DIR, file)))
      
df_final = pd.concat(df_list, ignore_index=True)
print(df_final, len(df_final))
import json

INPUT_FILE = "../../Data/student.json"

with open(INPUT_FILE, "r", encoding="utf=8") as f:
   data = json.load(f)
   
   for key, item in data.items():
      print(key)
      print(item)
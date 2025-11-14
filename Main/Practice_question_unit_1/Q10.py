import json

data = {"Product":"Laptop", "Price":55000, "Brand":"Dell"} 

with open(r"./Main/Practice_question_unit_1/Q10.json", "w", encoding="utf-8") as f:
   json.dump(data,f,indent=4)
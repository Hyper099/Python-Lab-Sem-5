try:
   num = int("101",base=2);
   print(num)
except ValueError as e:
   print("ValueError:",e);
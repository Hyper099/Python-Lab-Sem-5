import csv

def main():
  with open('../Data/students.csv', mode='r') as f:
    csvFile = csv.DictReader(f)
    for lines in csvFile:
      print(lines)


  
if __name__ == "__main__":
  main()
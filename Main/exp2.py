import csv

def calculae_avg(data):
  avg = round(sum(data) / len(data), 2)
  return avg


def main():
  main_data = []
  with open('../Data/students.csv', mode='r') as f:
    csvReader = csv.DictReader(f)
    for line in csvReader:
      student_avg = {}
      maths_marks = line['Maths']
      science_marks = line['Science']
      english_marks = line['English']

      data = [float(maths_marks), float(science_marks), float(english_marks)]       
      student_avg['Name'] = line['Name']
      student_avg['Average'] = calculae_avg(data)

      main_data.append(student_avg)

  fields = ['Name', 'Average']
  with open('student_average_grades.csv', 'w', newline='') as f:
    csvwriter = csv.DictWriter(f, fieldnames=fields)
    csvwriter.writeheader()
    csvwriter.writerows(main_data)
  

  
if __name__ == "__main__":
  main()
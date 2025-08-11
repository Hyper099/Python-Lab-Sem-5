import csv
import os

def calculae_avg(data):
  avg = round(sum(data) / len(data), 2)
  return avg

INPUT_DIR = '../Data/students.csv'
OUTPUT_DIR = '../Outputs/output_exp2'
os.makedirs(OUTPUT_DIR, exist_ok=True)

def main():
  main_data = []
  with open(f'{INPUT_DIR}', mode='r') as f:
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
  grades_csv = os.path.join(OUTPUT_DIR, 'student_average_grades.csv')
  with open(grades_csv, 'w', newline='') as f:
    csvwriter = csv.DictWriter(f, fieldnames=fields)
    csvwriter.writeheader()
    csvwriter.writerows(main_data)
  

if __name__ == "__main__":
  main()
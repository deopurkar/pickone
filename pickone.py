import csv
import random

def updateScores(choices, choice):
    with open("namesdb.csv", 'w') as file:
        csvwriter = csv.DictWriter(file, fieldnames=['Name','Score'])
        for i in range(0, len(choices)):
            if i == choice:
                choices[i]['Score'] = int(choices[i]['Score']) + 1
            else:
                choices[i]['Score'] = int(choices[i]['Score']) - 1
            csvwriter.writerow(choices[i])

def askAndUpdate():
  with open("namesdb.csv", 'r') as file:
      csvreader = csv.DictReader(file,fieldnames=['Name','Score'])
      lst = list(csvreader)
  choice1 = random.choice(lst)
  choice2 = random.choice(lst)
  choice = int(input("1. " + choice1['Name'] +"  2. " + choice2['Name'] +" : "))
  if choice == 0:
    return False

  updateScores([choice1, choice2], choice-1)

  return True

while askAndUpdate():
    print("-----------------------------")

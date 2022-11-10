import csv
import random

def updateScores(choices, choice):
    with open("namesdb.csv", 'w') as file:
        csvwriter = csv.DictWriter(file, fieldnames=['Name','Score'])
        for i in range(0, len(choices)):
            if i == choice:
                choices[i]['Score'] = float(choices[i]['Score']) * 1.1
            else:
                choices[i]['Score'] = float(choices[i]['Score']) / 1.1
            csvwriter.writerow(choices[i])

def getRandomElement(lst):
    totalScore = sum([float(pair['Score']) for pair in lst])
    runningScore = 0
    i = 0
    randomScore = random.random() * totalScore
    while runningScore < randomScore:
        i = i + 1
        runningScore = runningScore + float(lst[i]['Score'])
    return lst[max(i-1,0)]

def askAndUpdate():
  with open("namesdb.csv", 'r') as file:
      csvreader = csv.DictReader(file,fieldnames=['Name','Score'])
      lst = list(csvreader)
  choice1 = getRandomElement(lst)
  choice2 = getRandomElement(lst)
  choice = int(input("1. " + choice1['Name'] +"  2. " + choice2['Name'] +" : "))
  if choice == 0:
    return False

  updateScores([choice1, choice2], choice-1)

  return True

while askAndUpdate():
    print("-----------------------------")

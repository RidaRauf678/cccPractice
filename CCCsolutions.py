#S1 2015
'''
numbers = []
k = int(input())
total = 0

for num in range(k):
  num = int(input())
  if num != 0:
    numbers.append(num)
  
  else:
    numbers.pop()

for i in range(len(numbers)):
  total = total + numbers[i]

print(total)
'''
     
#S1 2016
'''
first = input()
second = input()
status = "0"

if len(first) == len(second):
  letters = len(second)
  lettersFirst = len(first)
  for letter in range(letters):
    letter = second[letters - 1]
    for letterFirst in range(lettersFirst):
      letterFirst = first[lettersFirst - 1]
      #how to check if all the letters in the string are the same as the first
      if letter == letterFirst:
        status = "N"
      elif letter == "*":
        status = "A"

print(status)
'''

#S1 2017
'''
n = int(input())
swiftRun = input()
semaphoreRun = input()
swiftTotal = 0
semaphoreTotal = 0
k = 0

swiftRuns = swiftRun.split(' ')
semaphoreRuns = semaphoreRun.split(' ')

for day in range(n):
  swiftTotal += int(swiftRuns[day])
  semaphoreTotal += int(semaphoreRuns[day])

  if swiftTotal == semaphoreTotal:
    k += 1

print(k)
'''

#S2 2015 - incomplete
'''
j = int(input())
a = int(input())
jerseys = []
numbers = [] 
count = 0


for num in range(a):
  numbers.append(num + 1)

for jersey in range(j):
  jersey = input()
  jerseys.append(jersey)

for athlete in range(a):
  athlete = input().split(" ") #ex ["L", "3"]

  toRemoveJ = ""
  toRemoveN = 0

  for jersey in range(len(jerseys)):
    if jerseys[jersey] == athlete[0]: #This checks if the size is available
        for n in range(len(numbers)):
          if int(athlete[1]) == numbers[n]:
            toRemoveJ = jersey
            toRemoveN = n
            count += 1
            
  if toRemoveJ != "" and toRemoveN != 0:
    numbers.pop(n)
    jerseys.pop(jersey)

print(count)
'''

#S2 2019 
'''
row = [1, 2]
row2 = [3, 4]


#put the flips in a list 
flipsList = []
flips = input()
for i in range(len(flips)):
  flipsList.append(flips[i])

#function for a vertical flip
def vertical(one):
  rowOne = []
  rowOne.append(one[1])
  rowOne.append(one[0])
  return rowOne

def vertical2(two):
  rowTwo = []
  rowTwo.append(two[1])
  rowTwo.append(two[0])
  return rowTwo

def horizontal(one, two):
  rowOne = []
  rowOne.append(two[0])
  rowOne.append(two[1])
  return rowOne

def horizontal2(one, two):
  rowTwo = []
  rowTwo.append(one[0])
  rowTwo.append(one[1])
  return rowTwo

one = row.copy()
two = row2.copy()

for i in range(len(flipsList)):
  if flipsList[i] == "H":
    oneOriginal = one.copy()
    one = horizontal(one, two)
    two = horizontal2(oneOriginal, two)
  
  elif flipsList[i] == "V":
    one = vertical(one)
    two = vertical2(two)

print(one)
print(two)
'''
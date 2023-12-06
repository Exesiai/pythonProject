#Austin Tran
#10-6-23
#mid term


import random

#the list empty
cutlist = []
for i in range(10):
    cutlist.append(0)

#adding random values
for index,value in enumerate(cutlist):
    cutlist[index] = random.randrange(0,11)

#length of list divided by two
listlen = int((int(len(cutlist)))/2)
del cutlist[listlen:]

def addthreetolist():
    newlist = []
    for i in range(3):
        newlist.append(random.randrange(0,11))
    return newlist

cutlist.extend(addthreetolist())

#function for cubing a number
def cubed(a):
   return a**3

finalList = (list(map(cubed,cutlist)))

def even(c):
    if c%2 == 0:
        return c

print(list(filter(even,finalList)))
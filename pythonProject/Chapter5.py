#Austin Tran
#9-25-23
#chapter 5


list1 =[4,'name',75.6,65,'hello']

#prints hello the end can start at -1 and then -2 then so on
print(list1[-1])

s = 'hello'

list1[1] = 'o'
print(list1)

word1 = 'python'
list2 = []
list2.append(word1)

print(list2)


#ca 1
list3 = [1,2,3,4,5,6,7,8,9,10]
print(list3)
def quad_list(listinp):
    for i in listinp:
        print(i*4,end=" ")

quad_list(list3)


#ca 2

tuple1 ='nice',

tuple2 = ([1,2,3,4],'nice')
tuple2[0][0] = 5

print("\n",tuple1,tuple2)

colors = ['red','orange','yellow']

#seems very useful for scan values in the lists
for index,value in enumerate(colors):
    print(index,value)

#ca3

list5 = [1,2,3,4,5,6,7,8,9,10]

print(list5[::-1])

print(len(list5))


#ca 4

numbers = []

for i in range(1,16):
  numbers.append(i)

print(numbers[1::2])

numbers[5:10] = [0]*5
print(numbers)

del numbers[5:]
print(numbers)

# del numbers[:]
# print(numbers)

numbers.sort(reverse=True)

print(numbers)


#ca5

rainbow = ['green','orange','violet']

rainbow.insert(rainbow.index('violet'),'red')
print(rainbow)

rainbow.append('yellow')
print(rainbow)

rainbow.reverse()
print(rainbow)

rainbow.remove('orange')
print(rainbow)


newlist = [2,3,4,6,6,5,4,5,7,8,9,5]

print(1 in newlist)

print(any(newlist))

def greaterthan(val):
    if val>4:
        return True
    else:
        return False
list7 = list(filter(greaterthan,[1,2,3,47,8,9]))

print(list7)

list8 =list(filter(lambda i: i>4 ,[1,2,3,47,8,9]))
print(list8)


#ca 6
def funct(val):
  if val%2 == 0:
      return True
  else:
      return False

newlists = list(map(funct,[1,4,5,12,6,7,33]))

print(newlists)


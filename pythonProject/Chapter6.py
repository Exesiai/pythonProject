#Austin Tran
#10-2-23
#chapter 6


# set1 = {1, 23, 3, 54, 6,677,8,1,1,1,1,1}
#
# print(set1)
#
dic1 = {'A':5,'B':6,'C':1}
#
# print(dic1.items())
#
for x,y in dic1.items():
    print(x,':',y)

print(dic1['A'])

list1 = [1,2,3,45,6,]
print(list1)

print(dic1)
dic1['C'] = 5
print(dic1)
#
# dic2 = {1:'i', 5:'v',10:'x',50:'l',100:'c',500:'d',1000:'m'}
#
# print(dic2[50]+dic2[5])


# dic1 = {'a':2,'b':3,'c':4}
#
# print(list(dic1.keys()))
#
# list1 = [4,4,5,6,7,2,3]
# for i in list1:
#     list1[i]=list1[5]
#
# print(list1)


set1 = {1,2,3,4,5,6}
# set2 = {1,2,3,4,5,6,8}
#
# print(set1|set2)
# print(set1.union(set2))
# print(set1&set2)
#
#
# import random
# mynum = random.randrange(1,1001)
# usnum = int(input("Give me a number from 1 to 1000: "))
#
# while mynum != usnum:
#     if mynum < usnum:
#         usnum = int(input('Number too high guess again: '))
#     else:
#         usnum = int(input('number is too low guess again: '))
#
# def add_two(num):
#     return num+2
#Austin Tran
#10-23-23
#chapter 8

var1 = 'hello world'
str1 = f'{2000000:>20,d}'

var2 = var1.split()

print(str1)
print(var1.strip())
print(var2)

print('hello' not in var1)

print(var1.replace('hello','goodbye'))
print(var1)


#ca1

#brute force
# name1 = f'{"Austin Tran":<22s}'
# name2 = f'{"Austin Tran":^22s}'
# name3 = f'{"Austin Tran":>22s}'
#
# print(name1)
# print(name2)
# print(name3)
#
# name = 'austin'
# list1 = ['<','^','>']
#
# #more iterable
# for i in range(3):
#   print(f'{name:{list1[i]}{2*len(name)}s}')


#ca2

str2 = 'found out for Fridays i\'m filling in for frank'

list1 = str2.split()

str3 = ''
for i in list1:
    if 'f' in i[0] or 'F' in i[0]:
        str3 += i+ " "

print(str3)


print(' '.join(list1))

import re
pattern = '02215'
ismatch = re.fullmatch(pattern,'02215')

if ismatch:
    print('true')
print('match' if re.fullmatch(r'\D{5}','abcde') else 'not match')
print('match' if re.fullmatch('[^A-Z][a-z]+','A') else 'not match')
print('match' if re.fullmatch('[A-Z]{5,7}','AAAAA') else 'not match')

#ca3

print('is a street name' if re.fullmatch('\d{2,3}\s\w+\s\w?','222 street name') else 'is not a street name')


#ca4
print(chr(65))
print(ord('A'))

print(ord('😑'))
print(chr(128529))

(printchr(0x1f643))
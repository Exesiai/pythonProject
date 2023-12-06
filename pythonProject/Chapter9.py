#Austin Tran
#11-3-23
#chapter 9


import os

with open('accounts.txt', mode='w') as accounts:
    accounts.write('100 Jones 24.98\n')
    accounts.write('200 Doe 345.67\n')
    accounts.write('300 White 0.00\n')
    accounts.write('400 Stone -42.16\n')
    accounts.write('500 Rich 224.62\n')

with open('accounts.txt', mode='r') as accounts:
    print(accounts)
    for record in accounts:
        account, name, balance = record.split()
        print(f'{account:<10}{name:<10}{balance:<10}')

accounts = open('accounts.txt','r')

temp_file = open('temp_file.txt','w')

with accounts, temp_file:
    for record in accounts:
        account, name, balance = record.split()
        if account != '300':
            temp_file.write(record)
        else:
            new_record = " ".join([account, 'William', balance])
            temp_file.write(new_record + "\n")


#ca1
with open('accounts.txt', mode='r') as accounts:
    print(accounts)
    for record in accounts:
        account, name, balance = record.split()
        if float(balance) >= 0:
            print(f'{account:<10}{name:<10}'+'Account OK!')
        else:
            print(f'{account:<10}{name:<10}' + "Insufficient Funds!")


try:
    8/0
except ZeroDivisionError:
    print('dumb dumb division by zero')
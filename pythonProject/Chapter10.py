#Austin Tran
#11-6-23
#chapter 10


class Account:
    """This keeps track of bank accounts"""
    def __init__(self,name,balance,interest_rate=0.02):

        self._name = name
        self._balance = balance
        self.interest_rate = interest_rate
        self.interest_income = 0


    def deposit(self,amount):
        """Deposit money into balance"""
        if amount <= 0.00:
            raise ValueError('Amount must be positive')
        self._balance += amount


    def withdraw(self,amount):
        """CA1 Withdraw money out of balance"""
        self._balance -= amount


ac1 = Account('nate',700.00,0.05)
print(ac1._name)
print(ac1._balance)

ac1.deposit(200)
print(ac1._balance)

ac1.withdraw(200)
print(ac1._balance)

#time class
"""Class time with read-write properties"""
class Time(object):
    """"""
    def __init__(self,hours = 0,minutes = 0,seconds = 0):
        self._hours = hours
        self._minutes = minutes
        self._seconds = seconds

    @property
    def hour(self):
        return self._hours

    @property
    def minute(self):
        return self._minutes

    @property
    def second(self):
        return self._seconds

    @hour.setter
    def hour(self,hour):
        if not(0 <= hour < 24):
            raise ValueError(f'Hour ((hour)) must be 0-23')
        self._hours = hour

    @minute.setter
    def minute(self,minute):
        if not(0 <= minute < 60):
            raise ValueError(f'Minute ((minute)) must be 0-59')

    @second.setter
    def second(self,second):
        if not(0 <= second < 60):
            raise ValueError(f'Second ((second)) must be 0-59')

    def __repr__(self):
        return 'this is the time'+" "+ str(self.hour) + ':'+str(self.minute)+":"+str(self.second)

    @property
    def time(self):
        return (self.hour,self.minute,self.second)

    @time.setter
    def time(self,time):
        if type(time) != tuple:
            raise ValueError('Input is not a tuple')
        if len(time) <3:
            raise ValueError('Tuple must be three items')

        self.hour = time[0]
        self.minute = time[1]
        self.second = time[2]


time1 = Time()
print(time1.hour)

print(time1.hour)

print(time1.time)

time1.time = (8,7,6)
print(time1)



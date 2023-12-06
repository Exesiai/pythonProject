#Austin Tran
#10-6-23
#mid term

import math

def triangle(a,b,c):
    if float(a) + float(b) + float(c) == 180:
        radA = math.radians(float(a))
        radb = math.radians(float(b))
        radc = math.radians(float(c))
        sineA = math.sin(radA)
        sineb = math.sin(radb)
        sinec = math.sin(radc)
        theTuple = (sineA,sineb,sinec)
        return theTuple
    else:
        print('these angles can\'t make a triangle')

newtuple = 'name','age',[3,5,7]

var1, var2, var3 = newtuple

print(newtuple)

del

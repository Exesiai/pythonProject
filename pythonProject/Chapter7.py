#Austin Tran
#10-9-23
#chapter 7
import math

import numpy as np
import random
# def count_by(x, n):
#     list1 = list(range(1,n+1))
#     for i,v in enumerate(list1):
#         list1[i] = v*x
#     return list1
#
#
# def reduce_fraction(fraction):
#     a,b = fraction
#     div = 0
#     step = 1
#     large = max(fraction)
#     small = min(fraction)
#     while large % (small / step) != 0:
#         step += 1
#         if step == small / 2:
#             return (fraction)
#     return (b / (small / step), a / (small / step))

ar1 = np.array([1,2,3,4])

print(ar1.dtype)

#ca1
ar2 = np.array([range(0,31,3)])

print(ar2)
print(ar2.size)
print(np.ones((5,5),str))
#
# import timeit
# print(timeit.timeit('"-".join(str(n) for n in range(100))',number=10000))
#
# def square(num):
#     return (num**2)
#
# #ca2
#
# list1 = range(0,600000
# np.random.randint(1,10,100000)
# print(timeit.timeit('np.random.randint(1,10,100000)',number=10000))


# ar1 = np.array([[3,4,5,6,7,8,9],[6,7,8,9,0,1,2],[6,7,8,9,0,1,2]])
#
# print(ar1)
#
# ar2 = ar1*5
#
# print(ar2)
#
# print(ar1.sum(axis=0))
#
# print(ar1[0:3])
#
# print(ar1[0:2,3])


#ca3

ar1 = np.array([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])

print(ar1[0])

print(ar1[1:3])

print(ar1[:,1:4])


# ar4 = np.array([1,2,3,4,5])
#
# ar5 = ar4.view()
#
# ar5[0] = 6
#
# print(ar4)


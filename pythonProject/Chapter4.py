#Austin Tran
#9-20-23
#chapter 4


# def square(param=4):
#   return param**2
#
# print(square())


#CW 1

# def sqrt(num=4):
#   return num ** (0.5)
#
# print(sqrt())


import random

# for roll in range(10):
#   roll1 = (random.randrange(1,7))
#   roll2 = (random.randrange(1, 7))
#   print(roll1,"-",roll2," Total:",roll1 +roll2)


#CW 2

# for flip in range(20):
#   side = random.randrange(0,2)
#   if side == 1:
#     print("flip",flip+1,"tails")
#   else:
#     print("flip",flip+1,"heads")

#teachers version
#
# heads = 0
# tails = 0
# for flips in range(20):
#   h_t = random.randrange(0,2)
#   if h_t == 0:
#     heads+=1
#     print("H",end="-")
#   else:
#     tails+=1
#     print("t",end="-")
# print()
# print("Heads",heads,"Tails",tails)

# def root_square(para):
#   root = para ** (.5)
#   square = para ** 2
#   return root , square
#
# rootnum,squarenum = root_square(9)
#
# print(rootnum)
# print(squarenum)
#
# int1 = 8
# # int1
# import math
# import statistics
# print(math.inf)


# def average(*args):
#   print(type(args))
#   return(args)
#   #return sum(args)/len(args)
#
# print(average([3,4,5,6,7]))


#cw 3

# import math
# def myfunc(*arges):
#     for i in arges:
#       if i == 0:
#         print("cant use zero")
#       else:
#         print(math.cos(math.pi/i))
#
# myfunc(1,2,3,0)

# str1 = "HELLO WORLD"
#
# print(str1.lower())

# str2 = 8
# print(str2.bit_count())

# import statistics as st
# st.mean()



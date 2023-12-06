# def pillars(num_pill, dist, width):
#     if num_pill == 1:
#       return 0
#     else:
#       return ((num_pill - 1) * dist * 100) - ((num_pill - 2) * width)
#
# print(pillars(2,20,25))



# def reduce_fraction(args=(1,1)):
#     a,b = args
#     c = a
#     d = b
#     if a<b:
#         while c != 0:
#             if a % c == 0 and b % c ==0:
#                 return(a/c,b/c)
#             c-=1
#     elif b<a:
#         while d != 0:
#             if a % d == 0 and b % d ==0:
#                 return(a/d,b/d)
#             d-=1
#
# print(reduce_fraction((1,1)))

# list1 = []
#
# list1.count()


#lasersquare
from math import sin
from math import tan
from math import radians

# theta = 60
# l = 1.8
# h = 0.5
#
# wl = 2/tan(radians(theta))
#
# lloverper = 2/sin(radians(theta))
#
# xval = (l/lloverper*wl)%1
#
# if xval//1!=0:
#     xval = 1 - xval
# else:
#     xval %= 1
#
# shift = h/2*wl
#
# shiftx = xval - shift
# yval= 0
# if (shiftx/wl) <= 0.5:
#         yval = (xval / wl)*2
# else:
#         yval = (1 - xval / wl)*2
#
# print(shift)
# print(wl/4)
# print(wl)
# print(lloverper)
# print(xval)
# print(yval)



# math.sin()
#
# def laser_coord(h, a, l):
#
#     if a > 0
#     elif a < 0
#     else
#
#     return (0, 0)

def array_diff(a, b):
    c = []
    for v in b:
        for i in a:
            if i != v:
                c.append(i)
    return c

print(array_diff([1,2,2],[]))
# yes = input("hi, do U wont to know ho you are in realty?   ")
# name = input("please enter your name to show U : ")


# def show(name):

#     if name.strip() == "hamza":
#         print("Oh , so sorry bro you are so fucking asshole go fuck your self peach")
#     else:
#         print("you are king of the all king around the world")


# show (name)


# d = ['ibra', 'haidar', 'hamod', 'hamza', 'man','efasf']
# h= dict (a)
# print(h)

# x = "wwwoooorrllddd"

# def clean (world):

#    if len (world) == 1 :
#       print(world)
#       return world

#    if world[0] == world[1]:
#       print(f"in convert {world}")
#       return clean(world[1:])
#    print(f"befor return:-------------- {world[0]}")
#    return world[0] + clean(world[1:])


# print(clean(x))


# 6! = 6x5x4x3x2x1

# hello = lambda name :print(f"hello your name is {name}")

# hello ("man")

# file = open("ibra.txt","w")
# for i in a :
#     file.writelines(f"{i}\n")
#     # file.writelines("\n")

# a = [-9,1,2,3,4,5,6,7]
# c="man utd football"

# print(c.ljust(22, " "), "x")

# from functools import reduce
# name = [ 1, 2, 3, 4, 5, 6, 7]
# newname= revesed(name)

# import termcolor
# import datetime
# # import pyf
# print(datetime.datetime.now().month)
# print(termcolor.colored("sada","green"))


# num = "ibrahem"
# iternum = iter(num)
# for i in range(7):
#     print(next(iternum,5),end="")
# def only_plus(fanc):
#     def inter(*num):
#         for i in num :
#             if i > 0 :
#                 o+=6
#                 continue
#             else:
#                 o-=6
#                 print("not plus interes value")
        
#         fanc(*num)
#     return (inter)

# from time import time

# def speed(func):
#     def real():
#         start = time()
#         func()
#         end = time()
#         print(f"    Fun time is : {end - start} sec")
#     return real

# @speed
# def sum():
#     for i in range (10000):
#         print(i)


# sum()

n = int(input("input num ").strip())
if n % 2 != 0:
   print("Werid")
elif n % 2 == 0 and n in range(2, 5):
    print("Not Weird")
elif n % 2 == 0 and n in range(6, 20):
    print("Werid")
elif n % 2 == 0 and n > 20:
    print("Not Weird")

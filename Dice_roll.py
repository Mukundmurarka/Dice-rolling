# import random
# print("It is a rolling dice")
# x = "y"
# while x =="y":
#     number = random.randint(1,6)
#     if number==1:
#         print("----------")
#         print("|         |")
#         print("|         |")
#         print("|    O    |")
#         print("|         |")
#         print("|         |")
#         print("-----------")
#     if number == 2:
#         print("----------")
#         print("|         |")
#         print("|         |")
#         print("| O     O |")
#         print("|         |")
#         print("|         |")
#         print("-----------")
#     if number == 3:
#         print("----------")
#         print("|         |")
#         print("|    O    |")
#         print("|    O    |")
#         print("|    O    |")
#         print("|         |")
#         print("-----------")
#     if number == 4:
#         print("----------")
#         print("|         |")
#         print("| O     O |")
#         print("|         |")
#         print("| O     O |")
#         print("|         |")
#         print("-----------")
#     if number == 5:
#         print("----------")
#         print("|         |")
#         print("| O     O |")
#         print("|    O    |")
#         print("| O     O |")
#         print("|         |")
#         print("-----------")
#     if number == 6:
#         print("----------")
#         print("|         |")
#         print("| O     O |")
#         print("| O     O |")
#         print("| O     O |")
#         print("|         |")
#         print("-----------")
#     x = input("press y for rolling again")
#
#

import sys
print(sys.getrecursionlimit())

def fun2(n):
    if (n == 0):
        return

    fun2(n / 2)
    print(n % 2, end="")
result = fun2(21)
print(result)


# def fact(n):
#     if n==0:
#         return 0
#     return (n+fact(n-1))
# result = fact(5)
# print(result)




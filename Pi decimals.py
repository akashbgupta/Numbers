import math
import sys
from decimal import *

#We use the Chudnovsky Algorithm to get the value of Pi up to n decimals

getcontext().rounding = ROUND_FLOOR
sys.setrecursionlimit(100000)

def factorial(n):
    if not n:
        return 1
    else:
        return n*factorial(n-1)

def iteratedvalue(k):
    k = k+1
    getcontext().prec = k
    sum = 0
    for k in range(k):
        first = factorial(6 * k) * (13591409 + 545140134 * k)
        down = factorial(3 * k) * (factorial(k)) ** 3 * (640320 ** (3 * k))
        sum += first / down

    return Decimal(sum)

def valuaofpi(k):

    iter = iteratedvalue(k)
    up = 426880 * math.sqrt(10005)
    pi = Decimal(up) / iter

    return pi

def shell():
    print(
        "Welcome to Pi Calculator. In the shell below Enter the number of digits upto which the value of Pi should be calculated or enter quit to exit")

    while True:
        print(">>> ", end='')
        entry = input()
        if entry == "quit":
            break
        if not entry.isdigit():
            print("You did not enter a number. Try again")
        else:
            print(valuaofpi(int(entry)))


if __name__ == '__main__':
    shell()





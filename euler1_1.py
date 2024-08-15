#!/usr/bin/env python
#https://projecteuler.net/


#project euler ex1 ###############

#
# def sumofmultiples35(maxnum, arr):
#     sum1 = 0
#     for i in range(1, maxnum):
#         if i % 3 == 0 or i % 5 == 0:
#             sum1 += i
#             arr.append(i)
#
#     return sum1
#
# arrg = []
# print(sumofmultiples35(1000, arrg))
# print(arrg)


#project euler ex2 ###############

# sum1 = 0
# tmp = 0
# first = 1; second = 2
# arr = []
# while tmp < 4000000 :
#     tmp = first + second
#     first, second = second , tmp
#     if tmp % 2 == 0:
#         sum1 += tmp
#         arr.append(tmp)
#
#
# print(sum1, arr)


#project euler ex3 ###############
from pprint import pprint


# def primefactor(num1, arr):
#     while num1%2 == 0:
#         num1 /= 2
#         arr.append(2)
#     while True:
#         min_multiplier = 3
#         range1 = range(min_multiplier, int(num1/min_multiplier)+2, 2)
#         for i in range1:
#             if num1%i == 0:
#                 num1 /= i
#                 arr.append(i)
#                 break
#         else:
#             print('finished')
#             arr.append(int(num1))
#             break
#
# num1 = 6008514
# arrg = []
# primefactor(num1, arrg)
# print(arrg, max(arrg))
#
# base1 = 1
# for i in arrg:
#     base1 *= i
# print(base1)





#project euler ex4 ###############


# def gainpalindrome():
#     strlist = [(i * j,i,j) for i in range(100,1000) for j in range(100,1000) if str(i*j) == str(i*j)[::-1]]
#     return strlist
# strlistg = gainpalindrome()
# pprint(strlistg)
# pprint(strlistg[-1])


# #project euler ex5 ###############
# import time
# def smallestmultiple(multiple):
#     number1 = multiple * 2
#
#     while True:
#         for i in range(2, multiple+1):
#             if number1 % i != 0 : break
#         else :
#             print("number found")
#             return number1
#         number1 += 2
# print(time.time())
# print(smallestmultiple(20))
#
# print(time.time())
#
#



# #project euler ex6 ###############

# n = 100
# squarelist = (i**2 for i in range(1, n+1))
# sumofsquare = sum(squarelist)
# sumlist = (i for i in range(1,n+1))
# squareofsum = sum(sumlist) ** 2
#
# print(squareofsum - sumofsquare)



# #project euler ex7 ###############


# def obtain_primenumber(nth, primelist):
#     quotily = 0
#     currentnumber = 5
#
#     while True:
#         for i in range(3, round(currentnumber/3)+2) :
#             if currentnumber % i == 0:
#                 break
#         else:
#             primelist.append(currentnumber)
#             quotily += 1
#         if quotily == nth - 2:
#             break
#         currentnumber += 2
#
#
#     return currentnumber


# primelistg = [2, 3]
# print(obtain_primenumber(10001
#                          , primelistg))
# pprint(primelistg)

# #project euler ex8 ###############
# import random
#
# def obtainmaxsum(strofdigits , quantity):
#
#     strofdigitlist = list(strofdigits)
#     patternlist =  strofdigitlist[:quantity]
#     del strofdigitlist[:quantity]
#     patternlist = [int(digit) for digit in patternlist]
#     sumofdigit = 1
#     for item in patternlist:
#         sumofdigit *= item
#     location =0; pointerofdigit = quantity
#
#     while True:
#         onemoredigit = int(strofdigitlist.pop(0))
#         patternlist.pop(0)
#         newpatternlist = patternlist + [onemoredigit]
#         prevsumofdigit = 1      #first digit not included
#
#         for item in patternlist:
#             prevsumofdigit *= item
#         nextsumofdigit = prevsumofdigit * onemoredigit
#
#         if sumofdigit < nextsumofdigit:
#             sumofdigit = nextsumofdigit
#             location = pointerofdigit - quantity + 1   #last digit's index
#
#         patternlist += [onemoredigit]
#
#         if pointerofdigit < len(strofdigits) - 1:
#             pointerofdigit += 1
#         else:
#             break
#
#     return sumofdigit, location
#
# thousanddigit = random.randrange(1e+20, 1e+21)
#
#
#
# strofdigits = str(thousanddigit)
# digit = '1234567890'
# strofdigits = ''.join([random.choice(digit) for i in range(100)])
#
#
#
# print(len(strofdigits))
# quantilyg = 13
#
#
# sum,location = obtainmaxsum(strofdigits, quantilyg)
#
# print(strofdigits)
# print(sum, location)
# print('pattern at index %d is %s' % (location, strofdigits[location: location+quantilyg]))



# #project euler ex9 ###############
#pythagorean triplet

# def obtaintriplet(sum):
#
#     for a in range(1,sum//2):
#         asquare = a ** 2
#         for b in range(a+1, sum//2):
#              if asquare + b ** 2 == (1000 - a - b) **2:
#                  return a , b
#
# ag,bg = obtaintriplet(1000)
# print()
# print( ag,'**2 + ' ,bg ,'**2 =',1000-ag-bg,'**2' )
#
# #project euler ex10 ###############
def obtain_primenumber(primelist, nth=0, upperlimit=0):

    quantily = 0
    currentnumber = 5

    while True:
        if currentnumber%3 != 0:
            for i in range(5, currentnumber//5 + 2) :
                if currentnumber % i == 0:
                    break
            else:
                primelist.append(currentnumber)
                quantily += 1
        if nth:
            if quantily == nth - 2:
                break
            else:
                currentnumber += 2
        else:
            if currentnumber >= upperlimit:
                break
            else:
                currentnumber += 2
        # print(currentnumber)

    return quantily


primelistg = [2, 3]
print(obtain_primenumber(primelistg, upperlimit=200000))

print(primelistg)

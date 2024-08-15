#!/usr/bin/env python
# euler problem 55
#
# If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.
#
# Not all numbers produce palindromes so quickly. For example,
#
# 349 + 943 = 1292,
# 1292 + 2921 = 4213
# 4213 + 3124 = 7337


# def reverse_num(number):
#     return int(str(number)[::-1])
#
#
# def main():
#     lychrellist = []
#
#     for number in range(10, 10000):
#         acc = 1
#         ori_number = number
#         while acc < 50:
#
#             number += reverse_num(number)
#
#             if number == reverse_num(number):
#                 break
#
#             acc += 1
#         else:
#             # print("lychrel:", ori_number)
#
#             lychrellist.append(ori_number)
#
#     print(lychrellist, len(lychrellist))
#
#
# if __name__ == '__main__':
#     main()

# euler problem 56
# A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.
#
# Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
# from functools import reduce
#
#
# def maxdigsum():
#
#     maxsum = finala = finalb = 0
#
#     for a in range(1, 100):
#         for b in range(1, 100):
#             number = a ** b
#             sumdigits = reduce(lambda x, y: x + int(y), str(number), 0)
#             if maxsum < sumdigits:
#                 maxsum, finala, finalb = sumdigits, a, b
#
#
#     print(maxsum, finala, finalb)
#
# if __name__ == '__main__':
#     maxdigsum()
##################################
# euler problem 57
# Square root convergents

# from fractions import Fraction
#
#
# def makefraction(prevnume: int, prevdemo: int):
#     return 2*prevdemo + prevnume , prevdemo+prevnume #nume, demo
#
#
# def islongernumorator(numo, demo ):
#     global acc
#
#
#
#     if len(str(numo)) > len(str(demo)):
#         print("found")
#         acc += 1
#
#
# acc = 0
#
#
# def main():
#     global acc
#     prevnumo = prevdemo = 1
#     for i in range(1000):
#         prevnumo, prevdemo = makefraction(prevnumo, prevdemo)
#         print(prevnumo ,'/', prevdemo)
#
#         islongernumorator(prevnumo, prevdemo)
#
#
#     print("final result:", acc)
#
# if __name__ == '__main__':
#     main()
#####################################
# Spiral primes
#
# Problem 58
# import math
#
# def findprime(num):
#     """
#
#     :param num:
#     :return: True or False
#     """
#     if not(num % 2):
#         return False
#     if num == 3:
#         return True
#
#     for i in range(3, int(math.sqrt(num))+1):
#
#         if not(num % i) :
#             return False
#     else:
#         print(num, end=' ')
#         return True
#
# def main():
#     mainnum = 1
#     layercount = 2
#     primecount = 0
#     while primecount == 0 or primecount / ((layercount-1)*4+1) > .10 :
#
#         for i in range(4):
#             mainnum += 2*layercount-2
#             isprime = findprime(mainnum)
#
#             if isprime:
#                 primecount += 1
#
#         layercount += 1
#
#     print("size of lenth:" , layercount*2 - 1)
#
#
#
# if __name__ == '__main__':
#     main()


#####################################
# XOR decryption
#
# Problem 59
# import math
#
# LOWER_CASE_ASCII = list(range(97, 123))
# UPPER_CASE = list(range(65, 91))
# SPACE = [32]
# WHOLE_ASCII = LOWER_CASE_ASCII + UPPER_CASE + SPACE
# KEY_LEN = 3
#
# from itertools import permutations, accumulate
#
#
# def genKeyList(len):
#     return \
#         permutations(LOWER_CASE_ASCII, len)
#
#
# def readfile(filename=".//p059_cipher.txt"):
#     with open(filename, 'r+') as file:
#         encrytedData = file.read().split(',')
#
#     return [int(elm) for elm in encrytedData]
#
#
# def main():
#     OriList = []
#
#     keyList = genKeyList(KEY_LEN)
#
#     encryptedData = readfile()
#
#     for key in keyList:
#
#         key = key * math.ceil(len(encryptedData) / 3)
#
#         orignalData = list(map(lambda a, b: a ^ b, encryptedData, key))
#
#         # print(orignalData)
#
#         isLetter = list(map(lambda ascii_letter: ascii_letter in WHOLE_ASCII, orignalData))
#
#         if all(list(isLetter)):
#             print(key, '#' , orignalData, "%", isLetter)
#             print(''.join(list(map(chr, orignalData))))
#             print(list(map(lambda key: chr(key), key[0:3])))
#
#             acc = accumulate(orignalData)
#             print("accumulated ASCII value is", list(acc)[-1])
#
#             break
#
#
# if __name__ == '__main__':
#     main()
#
#
# Problem 60
# Prime pair sets
# Show HTML problem content

# The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.
#
# Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

import math
from enum import Enum
from itertools import combinations, permutations


#
# def findprime(num):
#     """
#
#     :param num:
#     :return: True or False
#     """
#     if not(num % 2):
#         return False
#     if num == 3:
#         return True
#
#     for i in range(3, int(math.sqrt(num))+1):
#
#         if not(num % i) :
#             return False
#     else:
#         # print(num, end=' ')
#         return True
#
# def getprimeList( ):
#
#
#     number = 3
#
#     while True:
#
#         if findprime(number):
#            sendnum = (yield number)
#
#            if sendnum and sendnum > number :
#                number = sendnum - 1
#
#         number += 1
#
#
# NUM_PRIME = 5
#
# def getprimepairsets(primeList):
#
#
#     prime_grp_list = combinations(primeList, NUM_PRIME)
#
#     for primegrp in prime_grp_list:
#         numpair_list = permutations(primegrp, 2)
#         concatnumList = (int(str(numpair[0])+str(numpair[1])) for numpair in numpair_list)
#
#         if all(map(findprime, concatnumList)):
#
#             print()
#             print("found", primegrp, sum(primegrp))
#
#             break
#     else:
#         return False
#
#     return True
#
#
#
#
#
#
# primeList = []
# getprimeList_gen = getprimeList()
#
# for number in getprimeList_gen:
#     print(number, end=' ')
#     primeList.append(number)
#
#
#     if len(primeList) % 100 == 0:
#         if getprimepairsets(primeList):
#             getprimeList_gen.close()


# ------------------------------------------------

# Problem 61
# Cyclical figurate numbers
#

#
# triList = [n * (n + 1) // 2 for n in range(40, 145) if 1000 < n * (n + 1) // 2 < 10000]
#
# squareList = [n ** 2 for n in range(30, 100) if 1000 < n ** 2 < 10000]
#
# penList = [n * (3 * n - 1) // 2 for n in range(25, 85) if 1000 < n * (3 * n - 1) // 2 < 10000]
#
# hexList = [n * (2 * n - 1) for n in range(20, 75) if 1000 < n * (2 * n - 1) < 10000]
#
# hepList = [n * (5 * n - 3) // 2 for n in range(20, 75) if 1000 < n * (5 * n - 3) // 2 < 10000]
#
# octList = [n * (3 * n - 2) for n in range(15, 60) if 1000 < n * (3 * n - 2) < 10000]
#
#
# class NumberType(Enum):
#     Triangle = 1
#
#     Square = 2
#
#     Pentagonal = 3
#
#     Hexagonal = 4
#
#     Heptagonal = 5
#
#     Octagonal = 6
#
#
# GROUPS = [(NumberType.Triangle, triList), (NumberType.Square, squareList), (NumberType.Pentagonal, penList),
#           (NumberType.Hexagonal, hexList), (NumberType.Heptagonal, hepList), (NumberType.Octagonal, octList)]
#
#
# # GROUPS = [(NumberType.Triangle,triList), (NumberType.Square, squareList), (NumberType.Pentagonal, penList)]
#
# class Node:
#     '''
#
#     '''
#
#     def __init__(self, numType, data: int, nextNodes: list = None):
#
#         self.numType = numType
#         self.frontNum = data // 100
#         self.rearNum = data % 100
#         self.data = data
#
#         self.nextNodes = nextNodes
#
#     def setNextNodes(self, wholeNodeList, excludedTypes):
#
#         nextNodes = []
#         for node in wholeNodeList:
#
#             if self.rearNum == node.frontNum and node.numType not in excludedTypes:
#                 nextNodes.append(node)
#
#
#         self.nextNodes = nextNodes
#
#     def __str__(self):
#
#         return str(self.data)
#
#     def __repr__(self):
#
#         return str(self.data)
#
#
# def initNodes():
#     nodeList = []
#
#     for group in GROUPS:
#         for ele in group[1]:
#             node = Node(group[0], ele)
#             nodeList.append(node)
#
#
#
#     return nodeList
#
#
# def walkNodes(node: Node, nodeList, excludedTypes=None):
#     '''
#
#     :param node:
#     :param nodeList:
#     :param excludedTypes:
#     :return:
#     '''
#
#     global cyclicNums
#
#     if not excludedTypes:
#         excludedTypes = []
#
#     excludedTypes.append(node.numType)
#
#     node.setNextNodes(nodeList, excludedTypes)
#
#     if len(excludedTypes) == len(GROUPS):
#         if node.rearNum == cyclicNums[0] // 100:
#             cyclicNums.append(node.data)
#             print("found", cyclicNums)
#             print(sum(cyclicNums))
#             exit()
#         else:
#             return
#
#     if not node.nextNodes:  # empty list
#
#         return
#
#     for nextNode in node.nextNodes:
#         cyclicNums.append(node.data)
#
#
#         walkNodes(nextNode, nodeList, excludedTypes)
#         cyclicNums.pop()
#         excludedTypes.pop()
#
#
# # main
# nodeList = initNodes()
#
# for rootnode in nodeList:
#     cyclicNums = []
#
#     walkNodes(rootnode, nodeList)
#
#

# Problem 62
# Cubic permutations
#
#
# cubeMap = [(1, 1), (2, 8), (3, 7), (4, 4), (5, 5), (6, 6), (7, 3), (8, 2), (9, 9)]
#
#
# def isCube(num):
#     """
#
#     :param num:
#     :return: False or True
#     """
#
#     if abs(num ** (1 / 3) - round(num ** (1 / 3))) < 10e-6:
#         return True
#     else:
#         return False
#
#
# STARTNUM = 41063625
#
#
# def main():
#     """
#
#     :return:
#     """
#
#     minCubicPerNum = STARTNUM
#
#     while True:
#
#         countOfCubes = 0
#         foundPermList = []
#         numList = permutations(str(minCubicPerNum))
#
#         for numStr in numList:
#             num = int(''.join(numStr))
#             if not isCube(num):
#                 continue
#
#             else:
#                 if num not in foundPermList:
#                     foundPermList.append(num)
#                     countOfCubes += 1
#
#         else:
#             if countOfCubes >= 5:
#                 print("found", minCubicPerNum, foundPermList)
#                 exit()
#
#         minCubicPerNum += 1
#
#
# if __name__ == '__main__':
#     main()

# Problem 63 - Powerful Digit Counts
# The -digit number, , is also a fifth power. Similarly, the -digit number, , is a ninth power.
#
# How many -digit positive integers exist which are also an th power?


def obtainNDigit(num: int):
    """

    :param num: num
    :return:  n-digit
    """


    exponential = 0
    while True:

        tempResult = num // 10 ** exponential
        if tempResult >= 10:
            exponential += 1
        else:
            break

    return exponential + 1


expon = 1
totalNumberOfInt = 0
while True:
    for base in range(1, 10):

        if expon == obtainNDigit(base ** expon):
            print(expon, "-", base, "**", expon)
            totalNumberOfInt += 1

    if expon > obtainNDigit(base ** expon):
        print("less than exponential", expon, base)
        break

    expon += 1

print("totol number of these integers are:", totalNumberOfInt)
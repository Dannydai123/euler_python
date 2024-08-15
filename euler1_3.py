"""
this is the file that solved euler ex31 to ex53


"""


# #project euler ex31 ###############

# Coin sums
# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?


# 1p as (last digit), 2p as sec last digit, 5p as third last digit , etc.

# too slow as below
import itertools
# COUNTS = [2, 4, 10, 20, 40, 100, 200]
#
# VALUE = [100, 50, 20, 10, 5, 2, 1]
#
# resultlist = []
# numberofways = 0
#
# ranges = [range(x) for x in COUNTS]
# prev_lastdigit = 201
#
# for tupledigits in itertools.product(*ranges):
#     if tupledigits[-1] < prev_lastdigit:
#
#         total = 0
#         for i in range(len(tupledigits)):
#             total += tupledigits[i] * VALUE[i]
#
#         if total == 200:
#             print(tupledigits)
#             numberofways += 1
#             prev_tupledigits = tupledigits
#             if prev_tupledigits[-1] == 0:
#                 prev_lastdigit == 201
#             # resultlist.append(tupledigits)
#
# # pprint(resultlist, width=120, compact=True)
# # print(len(resultlist))
#
# print(numberofways)


################################################
### multiprocessing version using Manager ######
###                                       ######
################################################




# import itertools
# import multiprocessing
# from pprint import pprint
#
#
#
# COUNTS = [10, 20, 40,100,200]
#
# VALUE = [100, 50, 20, 10, 5,2, 1]
#
# resultlist = []
# numberofways = 0
# rangeslist = []
#
#
#
# for i in range(2):
#     for j in range(4):
#         if i == 1 and j == 3:
#             break
#         ranges = [range(i, i+1), range(j, j+1)] + [range(x) for x in COUNTS]
#
#         rangeslist.append(ranges)
#
# # pprint(rangeslist)
#
#
#
#
# def iterate(ranges,resultlist):
#
#     prev_lastdigit = 200
#     name = multiprocessing.current_process().name
#     print('p-'+ repr(ranges) +'process', 'running')
#     numberofways = 0
#     remaining = 200 - ranges[0][0] * VALUE[0] - ranges[1][0] * VALUE[1]
#     prefix_tupledigits = ranges[0][0], ranges[1][0]
#     if remaining == 0:
#         resultlist.append(1)
#         return
#     for tupledigits in itertools.product(*ranges[2:]):
#
#
#         if tupledigits[-1] < prev_lastdigit:
#
#             total = 0
#             for i in range(len(tupledigits)):
#                 total += tupledigits[i] * VALUE[i+2]
#
#             if total == remaining :
#
#                 # print(name+':', prefix_tupledigits + tupledigits)
#                 numberofways += 1
#                 # print(name, '-->', numberofways)
#                 prev_tupledigits = tupledigits
#                 if prev_tupledigits[-1] == 0:
#                     prev_lastdigit == remaining
#                 # resultlist.append(tupledigits)
#
#     resultlist.append(numberofways)
#
#
#
# jobs = []
# if __name__ == "__main__":
#
#     mgr = multiprocessing.Manager()  #Manager
#
#     resultlist =  mgr.list()
#     for ranges in rangeslist:
#         p = multiprocessing.Process(target=iterate,name='p-' + str(len(jobs)), args=(ranges,resultlist))
#         jobs.append(p)
#         print(p.name, 'starting')
#         p.start()
#
#
#
#     while True:
#         alive = 0
#         for j in jobs:
#             if j.is_alive():
#                 alive += 1
#                 j.join(timeout=1)
#                 print('Now {} running '.format(j))
#                 print(resultlist)
#         if alive == 0:
#             # all done
#             break
#
#
#     print(resultlist)


# #project euler ex32 ###############
# Find the sum of all products whose multiplicand/multiplier/product identity can be written
# as a 1 through 9 pandigital. like 39 × 186 = 7254
#
# import math
# from pprint import pprint
#
#
# def findmultipliers(number, resultlist):
#
#     # resultlist = []
#     for i in range(2, int(math.sqrt(number))+2):
#
#         if number % i == 0 and checkpandigital(number, number//i, i):
#             resultlist.append({'product': number, 'multipliers': (i, number//i)})
#
#
#
#
# def checkpandigital(number1,number2, number3):
#
#     """
#     :param number1:
#     :param number2:
#     :param number3:
#     :return:
#     """
#
#     strofnumber = str(number1) + str(number2) + str(number3)
#     if len(strofnumber) == 9 and set(strofnumber) == zerotonineset:
#         return True
#     else:
#         return False
#
#
# zerotonineset = set(map(str, range(1,10)))   #constant value
# resultlistg = []
# for i in range(1000, 10000):
#     findmultipliers(i, resultlistg)
#
# pprint(resultlistg, width=120, compact=True)
#
#
#
# productset = set((item['product'] for item in resultlistg))
#
# pprint(productset, width=120, compact=True)


# #project euler ex33 ###############
# Digit cancelling fractions

# from pprint import pprint
#
# resultlist = []
# for numerator in range(11,100):
#     for demomin in range(11,100):
#         if numerator/demomin < 1:
#
#
#
#
#             try:
#                 if numerator/demomin == (numerator//10)/(demomin%10) and numerator%10 == demomin//10 or \
#                    numerator/demomin == (numerator%10)/(demomin//10) and numerator//10 == demomin%10:
#
#                     resultlist.append((numerator, demomin))
#             except ZeroDivisionError:
#                 continue
#
#
#
# pprint(resultlist, width=120, compact=True) #[(16, 64), (19, 95), (26, 65), (49, 98)]
#
# nproduct=dproduct=1
#
# for n,d in resultlist:
#     nproduct *= n
#     dproduct *= d
#
# while True:
#
#
#     for i in range(2, nproduct + 1):
#
#         if nproduct%i == 0 and dproduct%i == 0:
#
#             nproduct //= i; dproduct //= i
#             break
#     else:
#         print('the end')
#         break
#
# print(nproduct, dproduct) #1 100





# #project euler ex34    ###############
# Digit cancelling fractions

# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.


# def factorial(num):
#     pass


# import math
# from pprint import pprint
#
#
# def obtainsum(num):
#
#     summ = 0
#     listofdigits = list(str(num))
#     for i in listofdigits:
#         summ += math.factorial(int(i))
#
#     return summ
#
# # main programme
# numberofdigits = 10
#
# listofresults = []
#
#
# for i in range(2, numberofdigits+1):
#     for j in range(10**(i-1), 10**i):
#
#         if j > math.factorial(9)*i:
#             break
#
#         elif j == obtainsum(j):
#             listofresults.append(j)
#
# pprint(listofresults, width=120, compact=True)
#
#
# print(sum(listofresults))
#
# #project euler ex35    ###############
#  circular primes
# using itertools as an experiment not good for this case
# because all rotations of the digits: 197, 971, and 719, are themselves prime, instead of 179,xx
# can not use permutation


#############################################################################
# import itertools
# import math
#
#
# def form_digits_ger():
#     for i in range(1, 5):
#         yield itertools.combinations(range(10), i)
#
#
# def isprime(number):
#     if number % 2 == 0:
#         return False
#     for divider in range(3, int(math.sqrt(number)) + 1):
#         if number % divider == 0:
#             return False
#     return True
#
#
# def permutation(com_digits, primelist):
#     digittuples = itertools.permutations(com_digits)
#     print(digittuples)
#     for digittuple in digittuples:
#
#         number = int(''.join(map(str, digittuple)))
#         if not isprime(number):
#             return
#
#     primelist.append(com_digits)
#
#
# def rotate(number):
#     numberstr = str(number)
#     return int(numberstr[1:] + numberstr[0])
#

# main

# digits_ger = form_digits_ger()
# for com_iter in digits_ger:
#
#     primelistg = []
#
#
#
#     for com_digits in com_iter:
#         # com_digits = (1, 9, 7)
#         if 0 in com_digits or 2 in com_digits or 4 in com_digits \
#             or 6 in com_digits or 8 in com_digits:
#             continue
#
#         permutation(com_digits, primelistg)
#
#     print(primelistg)
#

############################################################################
# simple way as below

# cirprimelistg = []
#
# for number in range(3, 10000):
#     orinumber = number
#
#     for i in range(len(str(number))):
#
#         if '0' in str(number) or not isprime(number):
#             break
#         else:
#             if i < len(str(number))-1:
#                 number = rotate(number)
#
#     else:
#         cirprimelistg.append(orinumber)
#
# print([2]+cirprimelistg)

# Problem 36 euler
# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million
#
# def ger_yieldpalindrome(uplimit):
#
#     for decimal in range(1, uplimit, 2):
#         if decimal == int((str(decimal)[::-1])) and bin(decimal)[2:] == bin(decimal)[-1:1:-1]:
#             yield decimal
#
#
#
# uplimit = 1000000
# for palindrome in ger_yieldpalindrome(uplimit):
#
#     print(palindrome)
#




# Problem 37 euler
#
# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.


#
#
# def findtruncprime(maxlimit):
#
#     import math
#
#     def isprime(number):
#
#         if number % 2 == 0 or number < 3:
#             return False
#         for divider in range(3, int(math.sqrt(number)) + 1):
#
#             if number % divider == 0:
#                 return False
#
#         return True
#
#
#     for anumber in range(11, maxlimit, 2):
#
#             notprimeflag = True
#
#             tempnumstr = str(anumber)
#             # tempnumstr = anumberstr[:-1]
#             while tempnumstr:
#                 if not isprime(int(tempnumstr)):
#                     notprimeflag = False
#                     break
#                 tempnumstr = tempnumstr[:-1]
#
#             tempnumstr = str(anumber)[1:]
#             while notprimeflag and tempnumstr:
#                 if not isprime(int(tempnumstr)):
#                     notprimeflag = False
#                     break
#                 tempnumstr = tempnumstr[1:]
#
#             if notprimeflag :
#                 print(anumber)
#                 yield anumber
#
#
#
#
# uplimit = 10000000000
# alist = []
# for index, thenumber in enumerate(findtruncprime(uplimit)):
#
#     alist.append(thenumber)
#
#
#     print(index, thenumber)
#     if len(alist) == 11:
#         break
#
#
#



# Problem 38 euler
# 192 × 1 = 192
# 192 × 2 = 384
# 192 × 3 = 576
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)
from pprint import pprint

# def find_pandigital(uplimit):
#
#     def ispandigital(basenumber):
#
#         joinednumber_asstr = ''
#         multiplier = 1
#         alist = []
#
#         initnumber = basenumber * multiplier
#         joinednumber_asstr = str(initnumber)
#
#         duplicatedigitflag = False
#
#         while len(joinednumber_asstr) < 9:
#
#             multiplier += 1
#             singlestepnumber = basenumber * multiplier
#
#
#             singlestepstringlist = list(str(singlestepnumber))
#
#             while singlestepstringlist:
#                 if singlestepstringlist.pop() in singlestepstringlist:
#                     return False, None, None
#
#             singlestepstringlist = list(str(singlestepnumber))
#             for everydigit in singlestepstringlist:
#                 if everydigit in joinednumber_asstr or everydigit == '0':
#                     duplicatedigitflag = True
#                     return False, None , None
#
#             else:
#                 joinednumber_asstr += str(singlestepnumber)
#
#         return True, multiplier, int(joinednumber_asstr)
#
#
#     # main def program
#
#     for basenumber in range(1, uplimit):
#
#         ispan, multiplier, pandigital = ispandigital(basenumber)
#
#         if ispan:
#             yield basenumber, multiplier, pandigital
#
#
#
#
# alist = []
# for obtainednumber in find_pandigital(10000):
#     alist.append(obtainednumber)
#     print(obtainednumber)
#
#
#
# alist.sort(key=lambda x: x[2], reverse=True)
# pprint(alist, compact=True, width=150)
#
#



# Problem 39 euler
'''If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?'''

import math

# def findintergralsolutions(number):
#
#
#     solutiondict = {}
#     solutiondict['solutions'] =[]
#     solutiondict['number'] = number
#     maxrightside = int(number / (2+math.sqrt(2))) + 1
#
#     for firstside in range(1, maxrightside):
#
#         for secside in range(1, (number-firstside)//2+1):
#             if firstside**2 + secside**2 == (number-firstside-secside)**2:
#
#                 solutiondict['solutions'].append((firstside, secside, number-firstside-secside))
#
#     if solutiondict['solutions']:
#         return solutiondict
#
#
#
# #main program
#
# uplimit = 1000
# resultset = []
# for number in range(1, uplimit+1):
#     solutiondictg = findintergralsolutions(number)
#     if solutiondictg:
#         resultset.append(solutiondictg)
#         # print(solutiondictg)
#
# resultset.sort(key=lambda x: len(x['solutions']))
#
# pprint(resultset, compact=True, width=120)
#
#


# problem 40 euler
# An irrational decimal fraction is created by concatenating the positive integers:


# numbersofdigits = [9, 90*2, 900*3, 9000*4, 9e5*5, 9e6*6] #reference for every number range's decimal'
#
# alist = []
#
# for i in range(1,7):
#     decimal = 10**i
#
#
#     for j in range(len(numbersofdigits)):
#         if decimal > numbersofdigits[j]:
#             decimal -= numbersofdigits[j]
#         else:
#             break
#     j = j - 1
#
#     basedecimal = 10**(j+1)
#
#     adecimal = decimal//(j + 2) + basedecimal - 1
#
#     if decimal%(j+2) == 0:
#         resultdigital = int(str(adecimal)[-1])
#     else:
#         resultdigital = int((str(adecimal+1))[decimal%(j+2) - 1])
#
#
#     print(resultdigital, basedecimal, adecimal)
#     alist.append((resultdigital, basedecimal, adecimal))
#
#
# print(alist)


# def shuixianhuahumber():
#     for i in range(100, 1000):
#         stri = str(i)
#         if int(stri[0])**3 + int(stri[1])**3 + int(stri[2])**3 == i:
#             print(i)
#
# shuixianhuahumber()




# problem 41 euler
# What is the largest n-digit pandigital prime that exists?For example, 2143 is a 4-digit pandigital and is also prime.


# def isprime(number):
#     if number % 2 == 0:
#         return False
#     for divider in range(3, int(math.sqrt(number)) + 1):
#         if number % divider == 0:
#             return False
#     return True
#
#
#
# from itertools import permutations
#
#
# ndigit = 1
# alist = []
# while ndigit <= 9:
#     for numbertuple in permutations(range(1, ndigit+1)):
#
#         number = int(''.join((str(item) for item in numbertuple)))
#
#         if isprime(number):
#             alist.append(number)
#
#     print(sorted(alist))
#
#     ndigit += 1
#


# Problem 42 euler
# Coded triangle numbers
#
# The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1);

# the word value for SKY is 19 + 11 + 25 = 55 = t10  is triangle word.
# given a file with thousands of words , obtain how many triangle words.
#
#
# def openfile():
#
#
#     def workout_trinum(wordstr):
#
#         asiilist = (ord(letter) - 64 for letter in list(wordstr))
#
#         if sum(asiilist) in trinumlist:
#             return wordstr
#
#
#
#     with open('p042_words.txt','r') as fd:
#
#
#         for line in fd:
#             for word in line.split(sep=','):
#                 word = word.strip('"')
#                 wordstr = workout_trinum(word)
#
#                 if wordstr:
#                     triwordlist.append(wordstr)
#
#
# #main progam
#
#
# trinumlist = []
# triwordlist = []
#
#
# for i in range(1, 41):
#     trinumlist.append(int(0.5*i*(i+1)))
#
#
# openfile()
# pprint(triwordlist, compact=True, width=120)
#
# print(len(triwordlist))
#
# print(trinumlist)
#
#######################################################################################
# Problem 43 euler
# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.
#
#
# from itertools import permutations
#
#
# resultlist = []
# primelist =[2,3,5,7,11,13,17]
#
#
# def getpandigitalnum(resultlist):
#
#
#     pandigital_iterable = permutations(range(10))
#
#     for digit_tuple in pandigital_iterable:
#         digitstr = ''
#         if digit_tuple[0] == 0: continue
#         for digit in digit_tuple:
#             digitstr += str(digit)
#
#         for i in range(7):
#
#             if int(digitstr[i+1: i+4]) % primelist[i] != 0:
#                 break
#         else:
#             print(int(digitstr))
#
#             resultlist.append(int(digitstr))
#
#
# getpandigitalnum(resultlist)
#
# print(resultlist)


#######################################################################################
# Problem 44 euler

# Pentagon numbers
#
# Problem 44
# Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten pentagonal numbers are:
#
# 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
#
# from collections import namedtuple
#
# pentagonlist = [1, ]
#
# specialpentagonlist = []
#
# Specialpentagon_struct = namedtuple('Specialpentagon_struct', ('currentpentagon', 'prevone', 'difference'))
#
#
#
#
# def getpentagonal_number():
#     # n = 2
#     for n in range(2, 10000):
#         pentagon = n*(3*n - 1) // 2
#
#         for prevpentagon in pentagonlist:
#
#             solvedn_sum = math.sqrt((pentagon + prevpentagon)*6 + 1/4) / 3 + 1/6
#             solvedn_diff = math.sqrt((pentagon - prevpentagon) * 6 + 1 / 4) / 3 + 1 / 6
#             if solvedn_diff == int(solvedn_diff)  and \
#                 solvedn_sum == int(solvedn_sum):
#
#                 pentagon_struct = Specialpentagon_struct(pentagon, prevpentagon,
#                                                          pentagon-prevpentagon)
#
#                 print(pentagon_struct)
#                 specialpentagonlist.append(pentagon_struct)
#
#         # print(pentagon)
#         pentagonlist.append(pentagon)
#
#
# getpentagonal_number()
# print(specialpentagonlist)
#
#
#
# Problem 45 euler
#
# Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
# Pentagonal	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
# Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...

# Find the next triangle number that is also pentagonal and hexagonal.


#
# import math
#
#
# def gettrianglenum(n: int):
#
#     while True:
#
#         triangle = n * (n+1) / 2
#         yield triangle
#         n += 1
#
#
# def ispentagonal(number: int):
#
#
#     resolved = math.sqrt((number) * 6 + 1 / 4) / 3 + 1 / 6
#
#     if resolved == int(resolved):
#         return True
#     else:
#         return False
#
#
# def ishexagonal(number: int):
#
#     resolved = (math.sqrt(number * 8 + 1) + 1)/4
#
#     if resolved == int(resolved):
#         return True
#     else:
#         return False
#
#
#
# globaln = 284
# gettrianglenum_ger = gettrianglenum(globaln)
#
# numberofresults = 0
#
# while numberofresults < 5:
#     candidate_num = next(gettrianglenum_ger)
#     if ispentagonal(candidate_num) and ishexagonal(candidate_num):
#         print(candidate_num)
#         numberofresults += 1
#



# Problem 46 euler
# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.


# def getprimer(startingnum, prime_list):
#     while True:
#         startingnum += 2
#         for i in range(3, int(math.sqrt(startingnum))+1, 2):
#             if startingnum % i == 0:
#                 yield startingnum    #yield a odd composite number
#                 break
#         else:
#             print('this is a prime', startingnum)
#             prime_list.append(startingnum)
#
#
#
#
#
# def determinenumbyrules(num, prime_list):
#
#     for prime in prime_list:
#         tempnum = math.sqrt((num - prime)/2)
#         if int(tempnum) == tempnum:
#             return True
#
#
#     return False
#
#
#
#
# primelist_global = [3]
# getprimer_ger = getprimer(3, primelist_global)
# resultnum = 0
#
# while not resultnum:
#     oddcompnum = next(getprimer_ger)
#     print(oddcompnum)
#
#     if determinenumbyrules(oddcompnum, primelist_global):
#         continue
#     else:
#         resultnum = oddcompnum
#
#
#
#
# print('the result number is', resultnum)
# pprint(primelist_global, width=120, compact=True)
#
#
#
#

# Problem 47 euler
#
# The first two consecutive numbers to have two distinct prime factors are:
#
# 14 = 2 × 7
# 15 = 3 × 5
# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

# def getprimer(startingnum, prime_list, upperlimit):
#
#     while startingnum < upperlimit:
#         startingnum += 2
#         for i in range(3, int(math.sqrt(startingnum))+1, 2):
#             if startingnum % i == 0:
#
#                 break
#         else:
#             # print('this is a prime :', startingnum)
#             prime_list.append(startingnum)
#
#
# def obtainconsecutiveint(numofdigits, prime_list):
#
#     # temp1 = 0
#
#     def obtainfactors(number):
#         devider = 3
#         factorlist = []
#         while number % 2 == 0:
#             factorlist.append(2)
#             number /= 2
#
#         while number != 1:
#             if number % devider == 0:
#                 number /= devider
#                 factorlist.append(devider)
#                 continue
#             devider += 2
#
#         return factorlist
#
#
# # main iteration
#
#     counter = 0  # a flag for the number of consecutive numbers
#     # for number in range(10 ** (numofdigits-1), 10 ** (numofdigits+2)):
#     number = 2
#     while True:
#         number += 1
#         if number in prime_list:
#             counter = 0
#             continue
#
#         factorlist = obtainfactors(number)
#         # print(factorlist)
#
#
#         factorset = set(factorlist)
#
#         if len(factorset) == numofdigits and factorset.issubset(prime_list):
#             counter += 1
#             if counter == numofdigits:
#                 return number - numofdigits + 1
#         else:
#             counter = 0
#
#
#
# # main program
#
#
# numberofdigits_g = 4
# primelist_g = [2,3]
# getprimer(3, primelist_g, 10**(numberofdigits_g+1))
# pprint(primelist_g, width=120, compact=True)
#
#
# result = obtainconsecutiveint(numberofdigits_g, primelist_g )
# print(result)
#
#
#



#
#
# Problem 48
# The series, 11 + 22 + 33 + ... + 1010 = 10405071317.
#
# Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.

# use future  concurrency module

from concurrent import futures


# def getsumofnumbertothepower(start, end):
#     """
#
#     :param start:
#     :param end:
#     :return: sum of the number to the power of that number
#     """
#     summary = 0
#     for number in range(start, end+1):
#         summary += number ** number
#
#     return summary
#
#
# print(getsumofnumbertothepower(1,1000))

# main program by using concurrent.future. not supported on Windows.

#
#
# maxdigit = 1000
# numofprocesses = 4
# # futurelist = []
# acc = 1
# finalresult = 0
#
# with futures.ProcessPoolExecutor(max_workers=4) as ex:
#     print('main: starting')
#     # while acc <= maxdigit:
#     #     lower = acc
#     #     upper = acc + maxdigit//numofprocesses if acc + maxdigit//numofprocesses <= 1000 else 1000
#
#     futurelist = [ex.submit(getsumofnumbertothepower, lower,  (lower+maxdigit//numofprocesses-1 if lower+maxdigit//numofprocesses-1 <=1000 else 1000) ) for lower in range(1, maxdigit+1, maxdigit//numofprocesses)]
#
#
#
#     # for f in futures.as_completed(futurelist):
#     #     print('main: result: {}'.format(f.result()))
#     #     finalresult += f.result()
#
#     print(futurelist)
# for f in futurelist:
#     finalresult += f.result()
#
# print(finalresult)
#
#
#
#
#
#
#
# Problem 49
#
# Prime permutations
#

# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
#
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.
#
# What 12-digit number do you form by concatenating the three terms in this sequence?
#
# from itertools import combinations,permutations,combinations_with_replacement
#
#
#
#
#
#
# def yieldpermuation():
#     combinationiter = combinations_with_replacement(range(0,10), 4)
#
#     for combination in combinationiter:
#         fourdigit_tuple_tuple = permutations(combination)
#
#         finalintegerlist = []
#         for fourdigit_tuple in fourdigit_tuple_tuple:
#             fourdigit_tuple= (str(digit) for digit in fourdigit_tuple)
#
#             fourdigit = int(''.join(fourdigit_tuple))
#             finalintegerlist.append(fourdigit)
#
#         if isrequiredone(finalintegerlist):
#             print('one found')
#
#
#
#
#
#
#
# def isrequiredone(integerlist):
#
#     founddigitslist = []
#     acc = 0
#
#     tempdigitslist = []
#
#
#     for integer in integerlist:
#         if integer > 1000 and  isprime(integer):
#             acc += 1
#             tempdigitslist.append(integer)
#
#     if acc >= 3:
#         founddigitslist = tempdigitslist[:]
#     if founddigitslist:
#         pairlistwithdiff = finddifference(founddigitslist)
#
#
#
#         result = equalseq(pairlistwithdiff)
#         if result:
#             print(result)
#             return True
#
#
#
# def equalseq(listwithdiff):
#
#     listwithdiff.sort(key=lambda x: x[2])
#
#     acc = 1
#     diff = -1
#     for tuple in listwithdiff:
#         if diff != tuple[2]:
#             diff = tuple[2]
#             prev_pair = sorted(tuple[:2])
#         else :
#             acc += 1
#
#             if doublecheck(prev_pair, sorted(tuple[:2])):
#                 return prev_pair,sorted(tuple[:2])
#
#
#
#
#
#
#
#
#
# def doublecheck(prev_pair, current_pair):
#     a,b,c,d = *prev_pair, *current_pair
#
#     if b==c and b-a == d-c and isprime(a) and isprime(b) and isprime(d) and a != b != d:
#
#
#         print(a,b,d)
#         return True
#
#
#
#
#
# def finddifference(founddigitslist):
#
#
#
#     # for integerlist in founddigitslist:
#
#     pairs_tuple = combinations(founddigitslist, 2)
#     pairlistwithdiff = []
#
#     for index, pair in enumerate(pairs_tuple):
#         pairlistwithdiff.append((*pair, abs(pair[0] - pair[1])))
#
#     # pprint(pairlistwithdiff, width=120, compact=True)
#     return pairlistwithdiff
#
#
#
#
# def isprime(number):
#     if number % 2 == 0:
#         return False
#     for divider in range(3, int(math.sqrt(number)) + 1):
#         if number % divider == 0:
#             return False
#     return True
#
#
#
# if __name__=='__main__':
#     yieldpermuation()

# problem 50
# The prime 41, can be written as the sum of six consecutive primes:
#
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# Which prime, below one-million, can be written as the sum of the most consecutive primes?
#
# def isprime(number):
#     if number % 2 == 0:
#         return False
#     for divider in range(3, int(math.sqrt(number)) + 1):
#         if number % divider == 0:
#             return False
#     return True
#
#
# def yieldprime(uplimit):
#     '''
#     :param uplimit:
#     :return:
#     '''
#     number = 5
#     while True:
#         if isprime(number):
#             yield number
#         number += 2
#
#
# #varibles of main block
#
# primelist_g = [3,2]
# uplimit = 1000000
# currentsumm = 0
# maxnumofprimes = 0
# yieldprime_ger = yieldprime(uplimit)
#
#
# def findsumofprimes(newprime, primelist):
#     '''
#
#     :param newprime:
#     :param primelist:
#     :return: True if found otherwise False
#     :global maxnumofprimes
#     '''
#
#     global maxnumofprimes
#     prevmaxnumofprimes = maxnumofprimes
#     summ = newprime
#     summwithmaxnumprimes = 0
#     for index, primefromlist in enumerate(primelist):
#
#         summ += primefromlist
#         if summ > uplimit:
#             break
#
#         if isprime(summ) and index+2 > maxnumofprimes:
#             maxnumofprimes, summwithmaxnumprimes= index+2, summ
#
#
#     if prevmaxnumofprimes < maxnumofprimes:
#         return True, summ, summwithmaxnumprimes
#     else:
#         return False, summ, 0
#
#
# #main loop
#
# while currentsumm < uplimit:
#
#     newprime = next(yieldprime_ger)
#
#
#     status, currentsumm, summwithmaxnumprimes = findsumofprimes(newprime, primelist_g)
#
#     if status:
#         print(maxnumofprimes, newprime, summwithmaxnumprimes)
#
#     primelist_g.insert(0, newprime)
#
#
#
#

# Problem 51 euler
# By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
#
# By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.
#
# Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
#
# import itertools
#
#
#
# def getpossiblecombinations(a, b):
#     '''
#
#     :param a: how many digits the number has
#     :param b: how many digits need to be replaced
#     :return: possiblecombined_tuple
#     '''
#
#     possiblecombined_tuple = itertools.combinations(range(1,a+1), b)
#
#     return possiblecombined_tuple
#
#
# def isprime(number):
#     if number % 2 == 0:
#         return False
#     for divider in range(3, int(math.sqrt(number)) + 1):
#         if number % divider == 0:
#             return False
#     return True
#
#
#
#
#
# def findprimeseq(chosenplaces: tuple, numberofdigits: int):
#     primeseqlist = []
#
#     # remainingplaces = numberofdigits - len(chosenplaces)
#
#     remainingplaces = tuple(set(range(1, numberofdigits+1)) - set(chosenplaces))
#
#
#     for everyrawdigit in range(10**len(remainingplaces)):
#
#
#
#         getone = docheck(everyrawdigit, remainingplaces, chosenplaces)
#
#
#         if getone:
#             primeseqlist.append(getone)
#             print(getone)
#
#
#     return primeseqlist
#
#
#
# def docheck(everyrawdigit, remainingplaces, chosenplaces):
#
#     basenumber = 0
#     for index, place in enumerate(remainingplaces, start=1):
#         index = len(remainingplaces) - index  # descend order
#
#         onedigit = everyrawdigit // (10 ** index)
#
#         everyrawdigit = everyrawdigit % (10 ** index)  #local variable everyrawdigit
#
#         basenumber += onedigit * 10 ** (place - 1)
#
#
#
#     numberofprimesinseq = 0
#
#     for digit in range(10):
#         finalnumber = basenumber
#         gern = [digit * 10 ** (everychosenplace - 1) for everychosenplace in chosenplaces] #a part of final number
#         finalnumber += sum(gern)
#
#         if finalnumber < 10 ** (a-1):
#             break
#
#         if not isprime(finalnumber):
#             numberofprimesinseq += 1
#         else:
#             pass
#             # print(finalnumber)
#         if numberofprimesinseq >= 3:
#             break
#
#     else:
#
#         return finalnumber , basenumber +  sum([0 * 10 ** (everychosenplace - 1) for everychosenplace in chosenplaces])
#
#     return 0
#
#
#
#
# #main program
#
#
# possiblemapping = [(a,b) for a in range(4,10) for b in range(2,9) if a > b ]
#
#
# print(possiblemapping)
#
# # possiblemapping = [(4, 2), (4, 3), (5, 2), (5, 3),]
#
# for a, b in possiblemapping:
#     possiblecombined_tuple = getpossiblecombinations(a, b)
#
#     for everycombination in possiblecombined_tuple:
#
#         primeseqlist = findprimeseq(everycombination, a)
#
#
#
#         print(a, ':',b,  primeseqlist)
#
#
#
# Problem 52 euler
# findpermutedmultiples

#
# def findpermutedmultiples(start: int, end: int, multiplier: int) :
#     """
#     :param start: starting number
#     :param end: ending number
#     :param multipler: 2x,3x,4x......
#     :return: smallest result or None if not found
#     """
#
#
#     for iternumber in range(start, end):
#         tempnumber = iternumber * multiplier
#
#         if set(str(iternumber)) == set(str(tempnumber)) and len(set(str(iternumber))) == len(str(iternumber)):
#             print('found one', iternumber, tempnumber, multiplier)  # TODO to be deleted
#             return iternumber, tempnumber, multiplier
#     return None
#
# resultlist = []
# for times in range(2, 7):
#
#
#     numberofdigits = 1
#     while True:
#         if numberofdigits % times == 0:
#             end = 10 ** numberofdigits // times
#         else:
#             end = 10 ** numberofdigits // times + 1
#
#         start = 10 ** (numberofdigits-1)
#
#         result = findpermutedmultiples(start, end, times)
#
#         if result:
#             resultlist.append(result)
#             break
#         numberofdigits += 1
#
# print(resultlist)

# Problem 53 euler
# Combinatoric selections
#
def findquatity(n: int,):
    """
    :param n:
    :param r:
    :return:
    """
    from math import factorial

    r = n // 2 #start from meadian
    value = factorial(n)/(factorial(r)*factorial(n-r))
    quatity = 0

    if value > 10**6:
        quatity = -1 if n//2 == n/2 else 0

        while value > 10**6:
            quatity += 2
            r -= 1
            value = factorial(n)/(factorial(r) * factorial(n-r))



    return quatity

acc = 0
for n in range(2, 101):


    incremented = findquatity(n)
    acc += incremented
    print('n=%d'%n, 'incremented by', incremented)

print(acc)



# decorator with parameter sample

def out_decor(arg1,arg2):

    d = 6

    def decor(fun):

        c = arg1


        def wrapper(*args, **kwargs):

            print('this is augmented function', c, d, arg2)

            fun(*args, **kwargs)
        return wrapper

    return decor


@out_decor('OUT', 'IN')
def afun(a, b):
    print(a, b)

# afun = out_decor('out')(afun)

afun(3,5)










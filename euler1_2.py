#!/usr/bin/env python
# https://projecteuler.net/

# #project euler ex11 ###############
#
# import random
# from pprint import pprint
#
#
# def generatematrix(matrix, width=20, height=20):
#
#     matrix[:] = [[random.randint(0, 99) for column in range(width)] for row in range(height)]
#
# def generatedictformatrix(bigmatrix):
#
#     dict = {}
#     maxsum = 0;maxsumat = ()
#     for row in range(len(bigmatrix)):
#         for column in range(len(bigmatrix[0])):
#             directionalsumlist = []  # including 8 sums of every directions.
#
#             directionalmatrix = getdirectionmatrix(row, column, 4)
#             dict[row, column] = []
#             for dirtuple in directionalmatrix:
#                 sum1 = 0
#                 for r,col in dirtuple:
#
#                     if r < 0 or r >= len(bigmatrix) or col < 0 or col >=len(bigmatrix[0]):
#                         sum1 = 0
#                         break
#
#                     else:
#                         sum1 += bigmatrix[r][col]
#
#                 dict[row, column].append(sum1)
#
#             tempsum = max(dict[row, column])
#             if tempsum > maxsum:
#                 maxsum = tempsum
#                 maxsumat = row, column
#             dict[row, column][0:0] = [ (tempsum,)]
#
#             # pprint(dict[row,column])
#
#     return dict,maxsum,maxsumat
#
# def getdirectionmatrix(x, y , length):
#
#
#     right = tuple((x+inc,y) for inc in range(length))
#     bottomright = tuple((x+inc,y+inc) for inc in range(length))
#     bottom = tuple((x,y+inc) for inc in range(length))
#     bottomleft =  tuple((x-inc,y+inc) for inc in range(length))
#     left = tuple((x-inc,y) for inc in range(length))
#     topleft = tuple((x-inc,y-inc) for inc in range(length))
#     top = tuple((x,y-inc) for inc in range(length))
#     topright =  tuple((x+inc,y-inc) for inc in range(length))
#
#     dirmatrix = [right, bottomright, bottom, bottomleft,left, topleft, top, topright]
#
#     return dirmatrix
#
#
# matrixg =[]
# generatematrix(matrixg,10,10)
#
# pprint(matrixg)
#
# dictg, maxsum, maxsumat = generatedictformatrix(matrixg)
#
#
# pprint(dictg)
# print(maxsum, maxsumat)

# #project euler ex12 ###############
# import math
# from pprint import pprint
#
#
# def getfactors(number):
#     """return a list of factors of this number
#
#
#     """
#     factorlist = []
#     for i in range(1, round(math.sqrt(number) + 0.5 + 1e-13)):
#         if number%i == 0:
#             factorlist.append(i)
#             factorlist.append(number//i)
#     return set(factorlist)
#
#
# natualnumber = 1
#
# triangelnum = 0
# factorslist = []
# while True:
#     triangelnum += natualnumber
#     factorsg = getfactors(triangelnum)
#     factorslist.append(factorsg)
#
#     if len(factorsg) > 15:
#         break
#     natualnumber += 1
#
# print(sorted(factorslist))
# print(triangelnum)
#


# #project euler ex13 ###############
# import random
#
# generator1 = (random.randrange(1e+49, 1e+50) for i in range(100))
# sum1 = 0
# for number in generator1:
#     print(number)
#     sum1 += int(str(number)[0:10])
#
# print('------------')
# print(sum1)
#
#
# #project euler ex14 ###############


# def getchain(number ,flag=0):
#
#     chainlist = []
#     while True:
#         chainlist.append(number)
#
#         if number != 1:
#             if number%2 == 1:
#                 number = 3*number + 1
#             else:
#                 number = int(number / 2)
#         else:
#
#             break
#     # listofchainlist.append(chainlist)
#     if flag == 0:
#         return len(chainlist)
#     elif flag == 1:
#         return len(chainlist),chainlist
#
# listofchainlistg = []
#
# maxlenofchain = 0; numberg = 0
# for i in range(1,1000000):
#     lengthofchain = getchain(i)
#
#     if maxlenofchain < lengthofchain:
#         maxlenofchain = lengthofchain
#         numberg = i
#
#
# print(numberg, maxlenofchain)
#
# print("max length of the chain %d , chain list as %s" % getchain(numberg,flag=1))

# #project euler ex15 ###############
#too slow for single process
from pprint import pprint

#
# def fun1(grid, resultlist):
#     counter = 0
#     # limitnumofdigit = 0   #sum up the number of '1'
#     for digit in range(2**grid-1, 2**(grid*2)+1):
#         binary = bin(digit)
#         if binary.count('1') == grid:
#            # print('{binary1:0>{width}s}'.format(binary1=binary[2:], width=2*grid))
#            counter += 1
#
#     return counter
#
#
#
#
#
#
# resultlistg = []
#
# for i in range(5):
#
#     counter = fun1(7, resultlistg)
#
# # pprint(resultlistg)
# print(counter)
#


#################################################################
#multiprocessing
#
# import multiprocessing
# import time
#
#
# class Consumer(multiprocessing.Process):
#
#     def __init__(self, task_queue, result_queue):
#         multiprocessing.Process.__init__(self)
#         self.task_queue = task_queue
#         self.result_queue = result_queue
#
#     def run(self):
#         proc_name = self.name
#         while True:
#             next_task = self.task_queue.get()
#             if next_task is None:
#                 # Poison pill means shutdown
#                 print('{}: Exiting'.format(proc_name))
#                 self.task_queue.task_done()
#                 break
#             print('{}: {}'.format(proc_name, next_task))
#             answer = next_task()
#             self.task_queue.task_done()
#             self.result_queue.put(answer)
#
#
# class Task:
#
#     def __init__(self, a, b, grid):
#         self.a = a
#         self.b = b
#         self.grid = grid
#
#     def __call__(self):
#         span = (self.a, self.b)
#         counter = 0
#         # limitnumofdigit = 0   #sum up the number of '1'
#         for digit in range(self.a, self.b ):
#             binary = bin(digit)
#             if binary.count('1') == self.grid:
#                 # print('{binary1:0>{width}s}'.format(binary1=binary[2:], width=2*grid))
#                 counter += 1
#
#         return span, counter
#
#     def __str__(self):
#         return 'range from {self.a} to {self.b}'.format(self=self)
#
#
# if __name__ == '__main__':
#     grid = 14
#     # Establish communication queues
#     tasks = multiprocessing.JoinableQueue()
#     results = multiprocessing.Queue()
#
#     # Start consumers
#     num_consumers = multiprocessing.cpu_count() * 2
#     print('Creating {} consumers'.format(num_consumers))
#     consumers = [
#         Consumer(tasks, results)
#         for i in range(num_consumers)
#     ]
#     for w in consumers:
#         w.start()
#
#     # Enqueue jobs
#     num_jobs = num_consumers
#     gridrange = int((2**(grid*2) - 2**grid) / num_jobs)
#     for i in range(num_jobs):
#         if i != num_jobs-1:
#             tasks.put(Task(2**grid-1 + gridrange*i, 2**grid-1 + gridrange*(i+1), grid))
#             print(bin(2**grid-1 + gridrange*i), bin(2**grid-1 + gridrange*(i+1)))
#         else:
#             tasks.put(Task(2 ** grid - 1 + gridrange * i, 2**(2*grid), grid))
#             print(bin(2 ** grid - 1 + gridrange * i), bin(2**(2*grid)))
#     # Add a poison pill for each consumer
#     for i in range(num_consumers):
#         tasks.put(None)
#
#     # Wait for all of the tasks to finish
#     tasks.join()
#
#     # Start printing results
#     print('------------------------------------------------')
#     gener_of_rangeandcounter = (results.get() for i in range(num_jobs))
#     results = sorted(gener_of_rangeandcounter, key=lambda result: result[0])
#     sum_counter = 0
#     for result,counter in results:
#         print('Range: from {range[0]:0>{width}b} to {range[1]:0>{width}b}'
#               .format(range=result, width=grid*2))
#         print('Range: from {range[0]:>10d} to {range[1]:>10d}'.format(range=result))
#         print('Counter:', counter )
#         sum_counter += counter
#     print('total counter:', sum_counter)





# #project euler ex16 ###############

# anumber = 2 ** 1000
# sum = 0
# for digitstr in str(anumber):
#     sum += int(digitstr)
#
# print(sum)


# #project euler ex17 ###############

# onedigitwordslist = ['','one', 'two', 'three', 'four', 'five', 'six','seven','eight',
#                    'nine']
#
#
# teenwordslist = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen',
#                'seventeen','eighteen',
#                'nineteen']
# twodigitwordslist =['','','twenty','thirty','forty','fifty','sixty'
#                     ,'seventy', 'eighty','ninety']
# hundredword = 'hundredand'
#
# totalnumofletters = 0
#
# for number in range(1,1000):
#     letterstr = ''
#     hundred_digit = number//100
#     number = number - 100*(number//100)
#     if hundred_digit != 0:
#         letterstr = onedigitwordslist[hundred_digit] + hundredword
#     if number == 0:
#          letterstr = letterstr[:-3]
#
#
#     sec_digit = number//10
#     if number > 19:
#
#         letterstr += twodigitwordslist[sec_digit]
#     elif 10<=number<=19:
#         letterstr +=  teenwordslist[number - 10]
#         print(letterstr)
#         continue
#
#     number = number - 10 * (number // 10)
#     letterstr += onedigitwordslist[number]
#
#     totalnumofletters += len(letterstr)
#     print(letterstr)
#
#
# print(totalnumofletters)
#


# #project euler ex18 and ex67 ###############
#same question but smarter method
#separate tranglelist into top and bottom parts, work out max value and join them.

# import random
#
#
# def built_triangle(totallevel):
#     trianglelist = [[random.randint(10, 99) for j in range(i)] for i in range(1,totallevel+1)]
#     return trianglelist
#
#
# def devide_triange(indextuple, level, trianglelist):
#     smalltrianglelist = []
#     for i in range(level+1):
#         slice = trianglelist[indextuple[0]+i][indextuple[1] : indextuple[1] + i+1]
#         smalltrianglelist.append(slice)
#     return smalltrianglelist
#
# def trianglepath(smalltriangelelist):
#
#     twodimlist = []
#     lenoflist = len(smalltriangelelist)
#
#
#     for i in range(int(2**(lenoflist-1))):
#         sublist = [smalltriangelelist[0][0]]
#         x = 0 ; subtotal = sublist[0]
#         for j in range(1,lenoflist):
#              x += i%2; i = i//2
#              newnumber = smalltriangelelist[j][x]
#              subtotal += newnumber
#              sublist.append(newnumber)
#
#         twodimlist.append((x, subtotal, sublist))
#
#     # pprint(twodimlist)
#
#     return twodimlist      #structure as[(lastnumber's index, subtotal, list),]
#
# def processmaxvalue(twodimlist):
#     # twodimlist1= []
#     totalmax = 0
#     totalmaxlist = [[i,0,[]] for i in range(len(twodimlist[0][2]))]
#     maxsum = 0
#     maxlist = []
#     for index,maxnumber,numberlist in twodimlist:
#         if maxnumber > maxsum:
#             maxsum = maxnumber
#             maxlist = numberlist
#         if totalmaxlist[index][1] < maxnumber:
#             totalmaxlist[index][1] = maxnumber
#             totalmaxlist[index][2] = numberlist
#
#
#
#
#     # for i in range(y+1):
#     #
#     #     for item in twodimlist:
#     #         if item[0] == i :
#     #             if item[1] > maxsum:
#     #                 maxsum = item[1]
#     #                 maxlist = item[2]
#     #     twodimlist1.append((i, maxsum, maxlist))
#     #     if maxsum > totalmax:
#     #         totalmax = maxsum
#     #         totalmaxlist = maxlist
#     return totalmaxlist, maxsum, maxlist
#
#
# def joindimlist(firstdimlist, secdimlist, startponit, joinedlist):
#
#     firstmax = firstdimlist[startponit][1]
#     firstmaxlist = firstdimlist[startponit][2]
#     for i in range(len(secdimlist)):
#
#         tempmax = firstmax + secdimlist[i][1] - secdimlist[i][2][0]
#         tempmaxlist =  firstmaxlist + secdimlist[i][2][1:]
#         joineditemmax = joinedlist[startponit+i][1]
#         if joineditemmax < tempmax :
#             joinedlist[startponit+i][1] = tempmax
#             joinedlist[startponit+i][2] = tempmaxlist
#
#     return None
# def rowdevide(row, twodimlist0):
#
#
#     indextuplegen = [(row, k) for k in  range(row+1)]
#
#     totalmax = 0
#     totalmaxlist = []
#
#
#
#     for item in indextuplegen:
#         smalltrianglelist = devide_triange(item, y, trianglelist)
#         # pprint(smalltrianglelist)
#
#         twodimlist = trianglepath(smalltrianglelist)
#
#         # pprint(twodimlist)
#
#         twodimlist1, totalmax1, totalmaxlist1 = processmaxvalue(twodimlist)
#
#         # pprint(twodimlist1)
#
#         # if twodimlist0[item[1]][1] + totalmax1 -totalmaxlist1[0] > totalmax:
#         #
#         #     totalmax  = twodimlist0[item[1]][1] + totalmax1 - totalmaxlist1[0]
#         #     totalmaxlist = twodimlist0[item[1]][2] + totalmaxlist1[1:]
#
#         #
#
#         joindimlist(twodimlist0, twodimlist1, item[1], joinedlist)
#         # print(joinedlist)
#
#
# #main
#
# import time
#
# y = 15
# trianglelist = built_triangle(y*4)
#
# # trianglelist =[
# #
# #
# #
# #               [44],
# #             [46, 84],
# #           [89, 80, 46],
# #         [73, 86, 27, 16],
# #       [38, 21, 85, 32, 64],
# #     [50, 26, 82, 21, 15, 13],
# #   [61, 67, 66, 87, 38, 45, 29],
# # [42, 72, 96, 36, 26, 23, 83, 56]]
#
#
#
# #smarter method start######################
# #first stage
#
# timea = time.time()
# smalltrianglelist = devide_triange((0,0), y, trianglelist)
# # pprint(trianglelist)
# twodimlist = trianglepath(smalltrianglelist)
#
# # pprint(twodimlist)
#
# twodimlist0, totalmax0, totalmaxlist0 = processmaxvalue(twodimlist)
#
# # pprint(trianglelist)
#
# joinedlist =[[j, 0, []] for j in range(y*4)]
#
#
# import copy
#
# rowdevide(y, twodimlist0)
# twodimlist0 = copy.deepcopy((joinedlist[:y*(1+1) + 1]))
# rowdevide(y*2, twodimlist0)
# twodimlist0 = copy.deepcopy((joinedlist[:y * (2 + 1) + 1]))
#
#
# # print(joinedlist)
#
#
# # indextuplegen = [(y, k) for k in range(y+1)]
# #
# #
# #
# # totalmax = 0
# # totalmaxlist = []
# #
# # joinedlist =[[j, 0, []] for j in range(y*3)]
# #
# # for item in indextuplegen:
# #
# #     smalltrianglelist = devide_triange(item, y, trianglelist)
# #     # pprint(smalltrianglelist)
# #
# #     twodimlist = trianglepath(smalltrianglelist)
# #
# #     # pprint(twodimlist)
# #
# #     twodimlist1, totalmax1, totalmaxlist1 = processmaxvalue(twodimlist)
# #
# #     # pprint(twodimlist1)
# #
# #     # if twodimlist0[item[1]][1] + totalmax1 -totalmaxlist1[0] > totalmax:
# #     #
# #     #     totalmax  = twodimlist0[item[1]][1] + totalmax1 - totalmaxlist1[0]
# #     #     totalmaxlist = twodimlist0[item[1]][2] + totalmaxlist1[1:]
# #
# #     #
# #
# #     joindimlist(twodimlist0, twodimlist1 , item[1], joinedlist)
# #     # print(joinedlist)
# #
#
#
#
#
# # print(totalmax, totalmaxlist)
#
#
# # sec stage calculation
# # twodimlist0 = joinedlist
#
# indextuplegen = [(len(twodimlist0) - 1, k) for k in range(len(twodimlist0))]
#
#
#
# totalmax = 0
# totalmaxlist = []
#
# # joinedlist =[(j, 0, []) for j in range(y*2)]
#
# for item in indextuplegen:
#
#     smalltrianglelist = devide_triange(item, len(trianglelist) - item[0] - 1, trianglelist)
#     # pprint(smalltrianglelist)
#
#     twodimlist = trianglepath(smalltrianglelist)
#
#     # pprint(twodimlist)
#
#     twodimlist1, totalmax1, totalmaxlist1 = processmaxvalue(twodimlist)
#
#     # pprint(twodimlist1)
#
#     if twodimlist0[item[1]][1] + totalmax1 - totalmaxlist1[0] > totalmax:
#
#         totalmax  = twodimlist0[item[1]][1] + totalmax1 - totalmaxlist1[0]
#         totalmaxlist = twodimlist0[item[1]][2] + totalmaxlist1[1:]
#
#
#
#
# print(totalmax , totalmaxlist)
# timeb = time.time()
# print('--------------------------------------')
#  smarter method end
#
# normal method takes way too long time
#
# twodimlist = trianglepath(trianglelist)
#
# # pprint(twodimlist)
#
# twodimlist0, totalmax0, totalmaxlist0 = processmaxvalue(twodimlist)
# print(totalmax0, totalmaxlist0)
# timec = time.time()
#
# print(trianglelist)
#
# print(timeb-timea)
# print(timec-timeb)

################################################################################

# #project euler ex19 ###############
#Counting Sundays and built a calendar

# class Calender:
#
#     MONTH = ['Jan','Feb','March','April','May','June','July','August','Sept','Oct','Nov','Dec']
#
#     DAYSOFMONTH = [31,28,31,30,31,30,31,31,30,31,30,31]
#
#     DAYS = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
#
#     def __init__(self, numberojyears, startyear=1900,startmonth='Jan',startdate=1,startday='Mon'):
#
#         self.numberofyears = numberojyears
#         self.startyear = startyear
#         self.startdate = startdate
#         self.startmonth = startmonth
#         self.startday = startday
#
#         self.year = startyear
#         self.month = startmonth
#         self.date = startdate
#         self.day = startday
#
#         self.datestructure = {'year': self.year,
#                           'Month': self.month,
#                           'dates': [],
#                           'days': []
#                           }
#
#         self.calentorcontainer = []
#     def construct(self):
#
#
#
#         def __workoutdayofJAN1(self):
#
#
#             month = self.MONTH.index(self.startmonth)
#             date = self.startdate
#
#             numbersofdaysfromJAN1 = date + sum(self.DAYSOFMONTH[:month])
#
#
#             day = (numbersofdaysfromJAN1-1) % 7
#             return self.DAYS[self.DAYS.index(self.startday) - day]
#
#
#         import copy
#         pointerofdayslist = 0
#
#         for yearth in range(self.numberofyears):
#             year = yearth + self.startyear
#             if (year%4 == 0 and year%100 != 0) or (year%4 == 0 and year%400 ==0):
#                 self.DAYSOFMONTH[1] = 29
#
#
#             self.datestructure['year'] = self.year = year
#
#             if yearth == 0:
#                 dayofJAN1 = __workoutdayofJAN1(self)
#                 self.day =  dayofJAN1
#
#             for monthth in range(12):
#                 dayslist = []
#                 dateslist = []
#                 # for date in range(1,self.DAYSOFMONTH[monthth]+1):
#                 dateslist = list(range(1,self.DAYSOFMONTH[monthth]+1))
#
#                 for date in dateslist:    #assign days
#
#                     dayslist.append(self.day)
#
#                     if self.day =="Sun":
#                         pointerofdayslist = 0
#                     else:
#                         pointerofdayslist += 1
#
#                     self.day = self.DAYS[pointerofdayslist]
#
#
#
#                 self.datestructure['Month'] = self.MONTH[monthth]
#                 self.datestructure['dates'] = dateslist
#                 self.datestructure['days'] = dayslist
#
#                 self.calentorcontainer.append(copy.copy(self.datestructure))
#
#
#
#     def countdays(self, day):
#         counter = 0
#         for datestructure in self.calentorcontainer:
#
#              counter += datestructure['days'].count(day)
#
#         print(day, "'s counter is ", counter)
#
#         return counter
#
#     def whatdayistoday(self,year,month,date):
#
#         for datestructure in self.calentorcontainer:
#             if datestructure['year'] == year and datestructure['Month'] == month:
#                 return datestructure['days'][date-1]
#         else:
#             return 'not found'
#
#
# numberofyears = int(input('number of years you want to see'))
#
#
# calandor = Calender(numberofyears, 2018,'Sept',16,'Sun')
# calandor.construct()
# pprint(calandor.calentorcontainer, indent=5, compact=True, depth=3,width=110)
#
# counter = calandor.countdays('Sun')
#
# print(counter)
#
# year = int(input('year of date'))
# month = input('month of date')
# date = int(input('the date'))
#
# day = calandor.whatdayistoday(year, month, date)
#
# print('the day of %s %s ,%s is %s' % (month, date, year, day))

# #project euler ex20 ###############

# def factorialdigit(n):
#     sum = 1
#     for i in range(1,n+1):
#         sum *= i
#     return sum
#
# digitsum = 0
# n = int(input('input a nubmer'))
# summary = str(factorialdigit(n))
# for digit in summary:
#     digitsum += int(digit)
#
# print(digitsum)


# #project euler ex21 ###############
#amicable number

# import math
# def amicable(n):
#     sumlist = [1]
#
#     for i in range(2, int(math.sqrt(n))+2):
#         if n%i == 0:
#             sumlist.append(i)
#             if n//i not in sumlist:
#                 sumlist.append(n//i)
#             else:
#                 break
#     return sum(sumlist)
#
#
# #main program
# tmp = 0
# amicablelist = []
# i = 2
# while i < 10000:
#     if i not in amicablelist:
#         amipair = amicable(i)
#         if i == amicable(amipair):
#             amicablelist.append(i)
#             if i != amipair:
#                 amicablelist.append(amipair)
#
#     i += 1
#     print(i)
#
#
# pprint(amicablelist, width= 120)
#


# #project euler ex22 ###############
#alphabatical order


# with open('.\\p022_names.txt', mode='r') as txtfile:
#     linestr = txtfile.readline()
# wordslist = linestr.split(sep='","')
#
# wordslist[0] = wordslist[0].strip('"')
# wordslist[-1] = wordslist[-1].strip('"')
#
# wordslist.sort()
# pprint(wordslist,width=120)
# total = 0
# for wordindex in range(len(wordslist)):
#     acc = 0
#     for letter in wordslist[wordindex]:
#         acc += ord(letter) - 64
#
#     total += acc * (wordindex+1)
#
#
# print(total)
#





# #project euler ex23 ###############

# Non-abundant sums
# import math
# from pprint import pprint
#
# def findabduntantnumber(abundantnumlist):
#
#     for number in range(12,28124):
#         tmp = 0
#         subsum = 1
#         for divider in range(2, int(math.sqrt(number))+2):
#             if number%divider == 0:
#                 subsum += divider
#                 subsum += number//divider
#         if subsum > number :
#             abundantnumlist.append(number)
#             print(number,subsum)
#
#
# def obtainpositiveint(abundantlist, resultlist):
#
#
#     for i in range(len(abundantlist)):
#         for j in range(i,len(abundantlist)):
#             temp = abundantlist[i] + abundantlist[j]
#             if temp <= 28123:
#                 resultlist.append(abundantlist[i] + abundantlist[j])
#
#
# abundantlistg = []
# resultlistg = []
#
# findabduntantnumber(abundantlistg)
# obtainpositiveint(abundantlistg, resultlistg)
#
# oldset = set(resultlistg)
# newset = set(range(1,28124)).difference(oldset)
# print(len(newset))
# pprint(newset, width=120,compact=True)
#
#



# #project euler ex24 ###############


#
#
# def obtainadigit(orderthofpermutations, digitlist ):
#     digitlist.sort()
#     if orderthofpermutations == 2 and len(digitlist) == 2:
#
#         return 1, 1
#
#     elif orderthofpermutations == 1 and len(digitlist) == 2:
#
#         return  0,1
#
#     else:
#
#         factorial = math.factorial(len(digitlist)-1)
#
#
#
#         if orderthofpermutations % factorial != 0:
#             times = orderthofpermutations // factorial  #index value
#         else:
#             times = orderthofpermutations // factorial - 1  #index value
#
#
#         extracted = times * factorial
#
#
#
#
#         return times , extracted
#
#
# numberofdigits = int(input('please give numbers of digits'))
# orderthofpermutations = int(input('an Nth of permutations'))
# import math
#
#
#
# # numberofdigits = 10
# # orderthofpermutations = 725760 + j
#
#
#
# summarylsit = []
#
#
# digitlist = list(range(numberofdigits))
# for i in range(numberofdigits - 1):
#
#
#         digit , extracted = obtainadigit(orderthofpermutations, digitlist)
#
#         orderthofpermutations -= extracted
#         summarylsit.append(str(digitlist.pop(digit)))
#
#
# summarylsit.append(str(digitlist.pop()))
#
# print(''.join(summarylsit))
#



# #project euler ex25 ###############

#1000-digit Fibonacci number

# fa = 1; fb = 1
# indexoffibo = 2
# print(1)
# print(1)
#
# while True:
#     fa, fb = fb, fa + fb
#
#
#
#     indexoffibo += 1
#     # print(fb)
#     if fb > 10 ** 999:
#
#         break
#
# print(indexoffibo, fb)



# #project euler ex26 ###############

## Reciprocal cycles

#
# import re
# TIMES = 10**2000
# recurrningnumberlist = []
# maxrecurring = 0
# digitofmaxrecurring = 0
# for i in range(2, 1000):
#
#     fractions = TIMES // i
#
#
#     matchobj = re.search(r'(\d+?)\1', str(fractions))
#
#     if matchobj and int(matchobj.group(1)) != 0:
#         lengthforecurring = len(matchobj.group(1))
#         recurrningnumberlist.append((i,lengthforecurring, '{:100d}'.format(fractions), '{:.100f}'.format(fractions/ TIMES)))
#
#         # print(matchobj.group(1))
#         if lengthforecurring > maxrecurring:
#
#             maxrecurring = lengthforecurring
#             digitofmaxrecurring = recurrningnumberlist[-1]
#
#
#
#
# # pprint(recurrningnumberlist, width= 320)
#
#
#
#
# print(maxrecurring)
# print(digitofmaxrecurring)
#
#
#


# #project euler ex28 ###############

#Number spiral diagonals


#
# def getnumsondiagonal(startnum, totallayer):
#     '''
#
#     :param startnum: new layer's start number
#     :param totallayer: the Nth of layer
#
#     :return: diagonalsum: the sum of diagonals
#     '''
#
#     diagonalsum = 1
#
#     for layer in range(1, totallayer+1):
#
#         temp = 2*layer
#
#         lowerright = startnum + temp - 1
#         lowerleft = lowerright + temp
#         upperleft = lowerleft + temp
#         upperright = upperleft + temp
#
#         diagonalsum += lowerright+upperleft + lowerleft + upperright
#
#
#         startnum = upperright + 1
#
#
#     return diagonalsum
#
# firstsum   = getnumsondiagonal(2, 500)
#
#
# print(firstsum)

# #project euler ex29 ###############

#Distinct powers


#
# limita = limitb = 100
#
# powerlist = (a**b for a in range(2, limita+1) for b in range(2, limitb+1))
#
# # pprint(powerlist, width=120, compact=True)
#
# # print(len(powerlist))
# print(len(set(powerlist)))



# #project euler ex30 ###############

# Digit fifth powers


# resultlist = []
#
# for number1 in range(2, 10*9**5):
#     subtotal = 0
#     for digit in list(str(number1)):
#         subtotal += int(digit) ** 5
#
#     if number1 == subtotal:
#         resultlist.append(number1)
#
# print(resultlist)




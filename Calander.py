#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:     Calendar
#
# Author:      শাইখ ইসলাম।
#
# Created:     01/06/2013
# Copyright:   (c) USER 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def leapyear(num):          # Checks about leapyear.
    if num % 4 == 0 and num % 100 != 0:
        return 1
    elif num % 400 == 0:
        return 1
    else:
        return 0

def firstday(num):          # Finds the first day(number) of a year.
    ref = 2000
    day = 0
    if num > ref:
        while ref < num:
            if leapyear(ref):
                day = day + 2
            else:
                day = day + 1
            ref = ref + 1
        day = day % 7
    else:
        while ref > num:
            if leapyear(num):
                day = day + 2
            else:
                day = day + 1
            num = num + 1
        day = 7 - (day % 7)
    return day

def month1stday(m,y):      # Finds the  first day(number) of a month in a year.
    c = firstday(y)
    sum = c
    mon = [0,31,28,31,30,31,30,31,31,30,31,30,31]
    if leapyear(y):
        mon = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    for i in range (m):
        sum = sum + mon[i]
    day = sum % 7
    return day

def daydate(d,m,y):            # Finds the day of date.
    x = month1stday(m,y)
    date = (d+x-1) % 7
    return date

def monthday(num,y):           # Returns num of day in month
     mon = [0,31,28,31,30,31,30,31,31,30,31,30,31]
     if leapyear(y):
        mon = [0,31,29,31,30,31,30,31,31,30,31,30,31]
     return mon[num]
def monthRet(num):                     # Prints the month as per num
    month = [0,"January","February","March","April","May","June","July","August","September","Octbor","November","December"]
    return month[num]

def month_print(m,y):
    print()
    str1 = "{0:>16} {1:<16}"
    str2 = "{0:^5}{1:^5}{2:^5}{3:^5}{4:^5}{5:^5}{6:^5}"
    print(str1.format(monthRet(m),y))
    print(str2.format("SAT","SUN","MON","TUE","WED","THU","FRY"))
    list1 = ["","","","","","",""]
    limit = monthday(m,y)
    for i in range(1,limit+1):
        p = daydate(i,m,y)
        list1[p] = i
        if p == 6:
            print(str2.format(list1[0],list1[1],list1[2],list1[3],list1[4],list1[5],list1[6]))
        if i == limit:
                for l in range(p+1,7):
                    list1[l] = ""
                return (str2.format(list1[0],list1[1],list1[2],list1[3],list1[4],list1[5],list1[6]))

def Day(day):               # Determines the day.
    if day == 0:
        return "Satarday"
    elif day == 1:
        return "Sunday"
    elif day == 2:
        return "Monday"
    elif day == 3:
        return "Tuesday"
    elif day == 4:
        return "Wednesday"
    elif day == 5:
        return "Thursday"
    elif day == 6:
        return "Friday"
    else:
        return "ERROR!"

x = input ("Enter a date/month/year :")
p = x.split(" ")

if len(p) == 3:
    d = int(p[0])
    m = int(p[1])
    y = int(p[2])
    if m <= 12:
        if d <= monthday(m,y):
            print(Day(daydate(d,m,y)))
        else:
            print("ERROR !!!")
    else:
        print("ERROR !!!")

elif len (p) == 2:
    m = int(p[0])
    y = int(p[1])
    if m <= 12:
        print(month_print(m,y))
    else:
        print("ERROR !!!")

elif len(p) == 1:
    y = int(p[0])
    for i in range(1,13):
        print(month_print(i,y))
        print()

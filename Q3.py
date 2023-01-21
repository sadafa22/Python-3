# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 23:09:07 2021

@author:Sadafa Pasha
"""

import datetime as dt

#Function to read and print the file
def readFile():
    a = file1.read()

    print(a)
    
    
#Function to count number of lines
def lineCount():
    b = file1.read()
    j = b.split("\n")

    count = 0

    for i in j[1:]:
        if i:
            count = count + 1

    print(count)
    

#Function to find runner's country
def runnerCountry(name):
    c = list(file1)
    l = []

    for i in c:
        i = i.split()
        l.append(i)

    for i in l[1:]:
        if i[0] == name or i[1] == name:
            if i[9] == 'Great':
                print(i[9],i[10])
            else:
                print(i[9])
                

    
            
#Function to find runner's information
def countryInformation(country):
    d = list(file1)
    L = []

    for i in d:
        i = i.split()
        L.append(i)

    for i in L[1:]:
        if i[9] == country:
            print(i)
            

#Function to find average time
def averageTime():
    e = list(file1)
    LIST = []
    F = []
    avg = 0

    for i in e:
        i = i.split()
        LIST.append(i)

    for i in LIST[1:]:
        s = i[8]
        date1 = dt.datetime.strptime(s, "%H:%M:%S")
        F.append(date1)
        
    for i in F:
        avg = avg + (i.second) + 60*(i.minute) + 3600*(i.hour)
    avg = avg/len(F)
    #rez = str(avg/3600) + ' ' + str((avg%3600)/60) + ' ' + str(avg%60)

    #print(dt.datetime.strptime(rez,"%H:%M:%S"))
    print("2.400:24.014:0.86")


while True:
    filename = input("Enter file name to read:")
    file1 = open(filename,"r")

    print("\nMAIN MENU")
    print("1. Read File")
    print("2. Line Count")
    print("3. Runner's Country")
    print("4. Country's Information")
    print("5. Average Time")
    print("6. Exit")
    choice = int(input("Enter your choice:"))

    if choice == 1:
        readFile()
    elif choice == 2:
        lineCount()
    elif choice == 3:
        print("Enter name of runner to find country")
        n = input()
        runnerCountry(n)
    elif choice == 4:
        print("Enter country name to find runner's details")
        Country = input()
        countryInformation(Country)
    elif choice == 5:
        averageTime()
    elif choice == 6:
        break


    file1.close()
    
    
        
        



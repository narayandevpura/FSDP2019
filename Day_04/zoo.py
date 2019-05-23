# -*- coding: utf-8 -*-
"""
Created on Fri May 10 15:45:12 2019

@author: Narayan Devpura
"""

"""
Code Challenge
  Name: 
    Zoo Management
  Filename: 
    zoo.py
  Problem Statement:
    Create different functions to :
    read the zoo.csv file using readlines and print them
    Print in list of animals in groups (elephant / tiger / lion / zebra / kangaroo)
    print the total number of water need by elephant / tiger / lion / zebra / kangaroo
    print the total number of water needed by all the animals    
"""
import csv
def Read():
    with open('zoo.csv') as file:
        csv_reader = csv.reader(file, delimiter=',')
        for line in csv_reader:
            print(line)

def Print():
    list_of_animals = set()
    with open('zoo.csv') as file:
        csv_reader = csv.reader(file, delimiter=',')
        next(csv_reader)
        for line in csv_reader:
            list_of_animals.add(line[0])
        
    
    print("Animals in zoo are: ",set(list_of_animals))

def WaterNeed():
    wn = {}
    with open('zoo.csv') as file:
        csv_reader = csv.reader(file, delimiter=',')
        next(csv_reader)
        for line in csv_reader:
            if line[0] in wn.keys():
                wn[line[0]] = wn[line[0]]+int(line[2])
            else:
                wn[line[0]] = int(line[2])
        print("Water Need By Animals: ")
        for k,v in wn.items():
            print("{0} : {1}".format(k,v))

def TotalWaterNeed():
    total = 0 
    with open('zoo.csv') as file:
        csv_reader = csv.reader(file, delimiter=',')
        next(csv_reader)
        for line in csv_reader:
            total += int(line[2])
    
    print('Total water need: ',total)



Read()
Print()
WaterNeed()
TotalWaterNeed()
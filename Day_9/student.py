# -*- coding: utf-8 -*-
"""
Created on Thu May 16 16:05:15 2019

@author: Narayan Devpura
"""

"""

Code Challenge 1
Write a python code to insert records to a mongo/sqlite/MySQL database 
named db_University for 10 students with fields like 
Student_Name, Student_Age, Student_Roll_no, Student_Branch.

"""
# using sqlite
import sqlite3
from pandas import DataFrame as DF

conn = sqlite3.connect("db_University.db")

c = conn.cursor()

c.execute("DROP TABLE STUDENT")
c.execute("""CREATE TABLE STUDENT(
        Student_Roll_No INT PRIMARY KEY NOT NULL,
        Student_Name TEXT NOT NULL,
        Student _Age INT NOT NULL,
        Student_Branch TEXT NOT NULL)""")

c.execute("INSERT INTO STUDENT VALUES(701,'ARYAN',20,'IT')")
c.execute("INSERT INTO STUDENT VALUES(702,'AZAN',21,'IT')")
c.execute("INSERT INTO STUDENT VALUES(703,'BHAVESH',20,'CSE')")
c.execute("INSERT INTO STUDENT VALUES(704,'CHIRAG',19,'ECE')")
c.execute("INSERT INTO STUDENT VALUES(705,'DAVID',20,'ECE')")
c.execute("INSERT INTO STUDENT VALUES(706,'GAMORA',20,'CSE')")
c.execute("INSERT INTO STUDENT VALUES(707,'FIROZ',21,'IT')")
c.execute("INSERT INTO STUDENT VALUES(708,'NEBULA',22,'IT')")
c.execute("INSERT INTO STUDENT VALUES(709,'TONY',23,'ME')")
c.execute("INSERT INTO STUDENT VALUES(710,'XANDRA',19,'EE')")

c.execute("SELECT * FROM STUDENT")

df = DF(c.fetchall(),columns = ['Student_Roll_no','Student_Name', 'Student_Age', 'Student_Branch'])
conn.commit()
conn.close()




# using mysql xampp

import mysql.connector
from pandas import DataFrame as DF

conn = mysql.connector.connect(user = 'root', password = '', host= 'localhost')

c = conn.cursor()

c.execute("CREATE DATABASE db_Universities")
c.execute('USE db_Universities')

c.execute("""CREATE TABLE STUDENTS(
        Student_Roll_No INT NOT NULL PRIMARY KEY,
        Student_Name TEXT NOT NULL,
        Student_Age INT NOT NULL,
        Student_Branch TEXT NOT NULL)""")

c.execute("INSERT INTO STUDENTS VALUES(701,'ARYAN',20,'IT')")
c.execute("INSERT INTO STUDENTS VALUES(702,'AZAN',21,'IT')")
c.execute("INSERT INTO STUDENTS VALUES(703,'BHAVESH',20,'CSE')")
c.execute("INSERT INTO STUDENTS VALUES(704,'CHIRAG',19,'ECE')")
c.execute("INSERT INTO STUDENTS VALUES(705,'DAVID',20,'ECE')")
c.execute("INSERT INTO STUDENTS VALUES(706,'GAMORA',20,'CSE')")
c.execute("INSERT INTO STUDENTS VALUES(707,'FIROZ',21,'IT')")
c.execute("INSERT INTO STUDENTS VALUES(708,'NEBULA',22,'IT')")
c.execute("INSERT INTO STUDENTS VALUES(709,'TONY',23,'ME')")
c.execute("INSERT INTO STUDENTS VALUES(710,'XANDRA',19,'EE')")

c.execute("SELECT * FROM STUDENTS")

df1 = DF(c.fetchall(),columns = ['Student_Roll_no','Student_Name', 'Student_Age', 'Student_Branch'])

conn.commit()
conn.close()





# using mongodb atlas (cloud)

from pymongo import MongoClient

client = MongoClient("mongodb://narayandevpura:narayan%407689099555@firstcluster-shard-00-00-kx92l.mongodb.net:27017,firstcluster-shard-00-01-kx92l.mongodb.net:27017,firstcluster-shard-00-02-kx92l.mongodb.net:27017/test?ssl=true&replicaSet=FirstCluster-shard-0&authSource=admin&retryWrites=true")


mydb = client.db_Universitys

def inserts(Student_Roll_No,Student_Name,Student_Age,Student_Branch):
     unique_student = mydb.STUDENTSS.find_one({"Student_Roll_No": Student_Roll_No})
     if unique_student:
        return "Student already exists"
     else:
        mydb.STUDENTSS.insert(
            {
                 'Student_Roll_No' : Student_Roll_No,
                 'Student_Name' : Student_Name,
                 'Student_Age' : Student_Age,
                 'Student_Branch' : Student_Branch   })
        return 'Student added successfully'
    
def fetch_all_student():
    user = mydb.STUDENTSS.find()
    for i in user:
        print (i)

inserts(701,'ARYAN',20,'IT')
inserts(702,'AZAN',21,'IT')
inserts(703,'BHAVESH',20,'CSE')
inserts(704,'CHIRAG',19,'ECE')
inserts(705,'DAVID',20,'ECE')
inserts(706,'GAMORA',20,'CSE')
inserts(707,'FIROZ',21,'IT')
inserts(708,'NEBULA',22,'IT')
inserts(709,'TONY',23,'ME')
inserts(710,'XANDRA',19,'EE')

fetch_all_student()






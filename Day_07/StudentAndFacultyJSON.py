# -*- coding: utf-8 -*-
"""
Created on Tue May 14 16:07:12 2019

@author: Narayan Devpura
"""
"""
Code Challenge
  Name: 
    Student and Faculty JSON
  Filename: 
    student.json
    faculty.json
  Problem Statement:
    Create a student and Faculty JSON object and get it verified using jsonlint.com
    Write a JSON for faculty profile. 
    The JSON should have profile of minimum 2 faculty members. 
    The profile for each faculty should include below information atleast:

        First Name
        Last Name
        Photo (Just a random url)
        Department 
        Research Areas (can be multiple)
        Contact Details (should include phone number and email id and can have multiple )
   Hint:
       www.jsonlint.com
       
"""

import json

Faculty = """[
        {
        "First Name" : "Sudeep",
        "Last Name" : "Mehta",
        "Photo" : "https://photo?q=sudeepmehta",
        "Department" : "CSE",
        "Research Areas" : ["Ml", "DL"],
        "Contact Details" : {
                "Mobile" : [9874563219,8745632149],
                "Email" : ["sudeep.mehta@gmail.com", "sudeep.cse@gmail.com"]
                }
        },
        {
        "First Name" : "Sujan",
        "Last Name" : "Mishra",
        "Photo" : "https://photo?q=sujanmishra",
        "Department" : "ECE",
        "Research Areas" : ["Semi-Conductors"],
        "Contact Details" : {
                "Mobile" : [9874365219,8778932149],
                "Email" : ["sujan.mishra@gmail.com", "sujan.ece@gmail.com"]
                }
        }
]"""
    
Student ="""[{
		"First Name": "Himanshu",
		"Last Name": "Bhangaria",
		"Father Name": "Manish Bagaria",
		"City": "Jhunjhuna",
		"State": "Rajasthan",
		"Branch": "Information Technology",
		"Mobile": 9874563652
	},
	{
		"First Name": "Harsimran",
		"Last Name": "Singh",
		"Father Name": "Manoj Singh",
		"City": "Ajmer",
		"State": "Rajasthan",
		"Branch": "Information Technology",
		"Mobile": 9874563652
	}
]
"""
with open("faculty.json", "w") as faculty:
    json.dump(Faculty, faculty)
    
with open("student.json", "w") as student:
    json.dump(Student, student)
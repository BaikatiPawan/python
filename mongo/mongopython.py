import pymongo
import json

from pymongo import MongoClient

connection = MongoClient("localhost", 27017)
db = connection.javaspace_db

# inserting data into db
#===================================
''' data_dict = {
    "_id" : 3,"ssn" : 101,"firstName" : "Vijay","lastName" : "Kumar","age" : 30,"gender" : "Male","email" : "vijay@gmail.com",
     "PhoneNumber" : [ { "mobileNo" : "9878025869","simType" : "PostPaid","provider" : "Vodafone","network" : "5G","type" : "Personal"}, 
         { "mobileNo" : "9494949898","simType" : "Prepaid","provider" : "Idea","network" : "4G","type" : "official"
         }
    ]
 }

 res = db.Person.insert_one(data_dict)

 print("inserted "+res.inserted_id)'''


data=db.Person

persons = data.find()

for person in persons:
        print(person)
        print("\n")
       


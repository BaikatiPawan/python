#reading a file
""" myfile = open("file/names.txt")
reader = myfile.read()
myfile.close()
print(reader) """

#reading file using "with" context manager

""" with open("file/names.txt") as myfile:
    reader =myfile.read()

print(reader) """

#read from one file write into another file

""" with open("file/names.txt") as namefile:
    reader = namefile.read()
    
with open("file/persons.txt","w") as personfile:
    personfile.write(reader)
    personfile.write("\nChennai\nBanglore") """

import time
import os

while True:
    if os.path.exists("file/person.txt"):
        with open("file/person.txt") as personfile:
            print(personfile.read())
        
    else:
        print("File does not exists...")
    time.sleep(5)


















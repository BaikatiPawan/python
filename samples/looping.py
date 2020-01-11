#iterating list using for loop

""" values =[8.9,6.4,7.8,9.5]
for value in values:
    print(round(value)) """

#iterating dictionary using forloop

""" personsdata ={"pawan":"9789831538","krishna":"9791064265","ust global":"1234567890"}
for person in personsdata.items():
    print(person)

for person in personsdata.items():
    print("{} has a phone number {}".format(person[0].title(),person[1]))

for key,value in personsdata.items():
    print("{} has phone number {}".format(key,value)) """

#iterating using while loop

""" username=" "
while username != "Pawan":
    username=input("Enter name : ") """

while True:
    username = input("Enter name ")
    if username == "Pawan":
        break
    else:
        continue

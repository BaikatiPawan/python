""" def mean(person):
    if type(person) == dict:
        mymean = sum(person.values())/len(person)
    else:
        mymean = sum(person)/len(person)
    return mymean


persondict ={"Pawan":2,"Vijay":4,"Ram":5}
print(mean(persondict))

#mylist =[2,3,4,5]
#print(mean(mylist)) """


""" def temperature(temp):
    if temp>30:
        return "Heat"
    else:
        return "cool"

#print(temperature(31))
value = int(input("Enter value : "))
print(temperature(value)) """

""" user_input = input("Enter your input : ")
message = "Hello %s!" %user_input;
message = f"Hello {user_input}"
print(message) """

#string formatting
name = input("Enter your name : ")
surname = input("Enter your surname : ")
greeting = "How are you...!"
message = "Hello %s %s %s" %(name,surname,greeting)

message = "Hello {} {} {} Hope you are doing well...!".format(name,surname,greeting)
print(message)
















""" my_temperature = [221,102,570,950,-9999,119]

result = []
for temperature in my_temperature:
    result.append(temperature/10)

print(result) """

""" my_temperature =[570,119,517,950,102]

result = [temp/10 if temp!=-9999 else 0 for temp in my_temperature ]

print(result) """



print([i*2 for i in [1,2,3,4,5]])

print([i*2 if i>0 else 0 for i in [0,4,-1,4,2,-7,-5,7,-8,-9]])






















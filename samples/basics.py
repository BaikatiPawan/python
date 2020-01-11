import datetime
mynow = datetime.datetime.now()
print(mynow)

name="Pawan Kumar"
print("Name : ",name)

x=10
y='10'
z=10.5
sum1 = x+x
sum2 = y+y
print(sum1,sum2)
print(type(x),type(y),type(z))

a=list(range(1,10))
print(a)

b= list(range(1,10,3))
print(b)

text= "hello"
print(text.upper())
print(text.title())

values=[10,2.8,3.2]
mysum=sum(values)
length = len(values)
meanValue = mysum/length
print(meanValue)
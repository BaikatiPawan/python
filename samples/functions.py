""" def area(a=2,b):
    return a*b

print(area(3,4)) """

""" def mean(*args):
    return sum(args)/len(args)

print(mean(1,4,5,2,7)) """

def find_max(*args):
    return max(args)


print(find_max(7,2,32,51,95,102,119))

def find_winner(**kwargs):
    return max(kwargs)

print(find_winner(Pawan=98,Kumar=89,Ramu=79,Sag=52,Bom=35))
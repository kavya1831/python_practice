import math

def log(a=10):
        if a>0:
            #a = int(input("enter a number to get log value"))
            X = math.log(a)
            print(X)
        else:
            print("not in range")

a =int(input("enter a number to get log value"))
log(a)





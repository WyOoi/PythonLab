import math

def add(x,y):
    ans = x+y
    print(x, " + ", y, " = ", ans)

def sub(x,y):
    ans = x-y
    print(x, " - ", y, " = ", ans)

def mul(x,y):
    ans = x*y
    print(x, " x ", y, " = ", ans)

def div(x,y):
    ans = x/y
    print(x, " 5 ", y, " = ", ans)

def sqr(x):
    ans = math.sqrt(x)
    print(" square root of ", x, " is ", ans)
    
print("1. add")
print("2. subtrate")
print("3. multiply")
print("4. divide")
print("5. square root")
print("6. exit")

choice = int(input("select operation from 1, 2, 3, 4, 5: "))
x= int(input("enetr 1st num: "))
y= int(input("enetr 2nn num: "))

if (choice==1):
    add(x,y)
elif(choice==2):
    sub(x,y)
elif(choice==3):
    mul(x,y)
elif(choice==4):
    div(x,y)
elif(choice==5):
    sqr(x)
elif(choice==6):
    print("exittttt")
    break
else:
    print("invalid operations")
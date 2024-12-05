names = open("names.txt","r")
x  = names.readlines()
names.close()
print(x)

x.sort()
print(x)
Snames = open("sortednames.txt","w")
for y in x:
    Snames.write(y)

Snames.close()
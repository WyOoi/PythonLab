keys = ["ten","twenty", "thirty"]
values = [10,20,30]

number = dict()
print(number)

for i in range(len(keys)):
    number.update({keys[i]:values[i]})

print(number)

newdict = {"banana":100, "watermelon":200, "orange":400}
new2dict = number.copy()
new2dict.update(newdict)
print(new2dict)

if 10 in new2dict.keys():
    print("yes")
else:
    print("no")

for i in new2dict:
    print(i , ":" , new2dict[i])
    total = total + new2dict[i]

print("total value: " , total)
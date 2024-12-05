# mytext = " hello my name is {0}".format("siti","aisyah")
# print (mytext)

################################################ 

# name = ["ali","abu","ahmad"]
# age = ["17","18","19"]

# for i in range(3):
#     mytext = " hello my name is {0}, my age is {1}".format(name[i],age[i])
#     print (mytext)

################################################

# mytext = "pi in three decimal point is: {0: .3f}".format(3.14129875)
# print(mytext)

# for i in range(4): 
#     print("{0:<7} {1:^7} {2:>7}".format("|||","---","///"))

# for i in range(10):
#     print(i+1 , " x " , "9: {0:>5}".format(i+1*9))

##################################################################################

mylist = [1,2,4,5]
mylist2 = ["hello","world"]
mylist3 = [1234,"heloo world", 2.6,[1,2,3,4]]
emptylist = []

print(mylist3[3][2]) # print the third index and (value inside the index index 2)
print(mylist3[2])
print(mylist,mylist2,mylist3,emptylist)

mylist[2] = 3 # replace value in index 2 become '3'
print(mylist)

for index in mylist3:#print the index in the list one by one
    print(index)

newlist = mylist + mylist2 # combine both 2 list become new list
print (newlist)
newlist[2:5] = [16,17,"beee"]
print(newlist)
newlist.append(100) # add the value 100 inside the end of the list
print(newlist)
newlist.extend(mylist)
print(newlist)

mylist4 = [ "d" , "a" , "c", 'h']
mylist4.sort()
print(mylist4)

mylist5 = ['11','33','4','99']
mylist5.sort()
print (mylist5)
# print(sum(mylist5))
mylist5.pop(2)
print(mylist5)
mylist5.append(100)
mylist5.remove(100)
print(mylist5)
del mylist5[1:3]
print(mylist5)

name ="aisyah"
namelist = list (name)
print (namelist)
print( namelists[4])

mytext = "this-is-utem"
mynewlist = mytext.split("-")
print(mynewlist)

sambung = " "
newtext = sambung.join(mynewlist)
print(newtext)

lists
# print(newlist * 3) # print three time this list
# print(newlist[1:3])
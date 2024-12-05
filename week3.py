i=2
x="aisyah"
print(x[i+2])
print(x[0])
print(x[len(x)-1])

panjang = len(x)
lastalpha = [panjang-1]
print(lastalpha)

i=0
while i < len(x):
    print(x[i])
    i+=1

for eachalpha in x:
    print(eachalpha)

#####################################

mytext = 'glt'
sambung = 'una'

for i in mytext:
    print(i+sambung)

print (x[2:6])
print(x[3:3])

######################################

word = 'elephant'
word2  = 'ferret'

if word < word2:
    print(word +"comes before" + word2)
elif word > word2:
    print(word +"comes after" + word2)

print ("s" in word)

########################################

animal = 'elephant is a not cute animal'
count =0
whichalpha ='p'

for i in animal:
    if i == whichalpha:
        count = count+1

print ("number of " + whichalpha + ":" + str(count))
print(animal.find("pha"))
myarray = animal.split()
print(myarray)
print(myarray[3])
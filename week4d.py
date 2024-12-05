mytuple = (1,2,3,4,5,6)
print(mytuple)

keyword = "hello world"
wordtuple = tuple(keyword)
print(wordtuple)

print(wordtuple[1:5])

wordtuple2 = ("h",) + wordtuple[1:]
print(wordtuple2)
wordtuple2 = wordtuple[0:6] + ("W" , ) + wordtuple[7:]
print(wordtuple2)

a= (1,2,3,700,4,500)

def myminmax(passtuple):
    return min(passtuple), max(passtuple)

printminmax = myminmax(a)
print(printminmax)

for i in range (-1, -12, -1):
    print(wordtuple2[i], end = "")

a= (1,2,3,700,4,500)
print()
b,c,d,e,f,g = a
print(e)

# a = (1,2,3)
# b = (4,5,6)

# a,b = b,a
# print(a)
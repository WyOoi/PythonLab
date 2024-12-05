# myfile = open("test.txt","w")
# myfile.write("hello world")
# myfile.write("-------\n")
# myfile.write("Welcome.....\n")
# myfile.close()

readfile = open("test.txt","r")
while True:
    x = readfile.readline()
    if len(x) ==0:
        break
    print(x,end="")

readfile.close()
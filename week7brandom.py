import random

osom = ["burung", "air", "batu"]

computer = random.choice(osom)
##print(computer)

user = input("Pilih apa woiiiii: ")

while(True):

    print(" User choose ", user)
    print(" Computer choose ", computer)

    if (user == "air"):
        if(computer == "air"):
            print("same")
        elif (computer == "burung"):
            print("computer win")
        elif (computer == "batu"):
            print("user win")

    elif (user == "burung"):
        if(computer == "burung"):
            print("same")
        elif (computer == "air"):
            print("user win")
        elif (computer == "batu"):
            print("computer win")

    elif (user == "batu"):
        if(computer == "batu"):
            print("same")
        elif (computer == "burung"):
            print("computer win")
        elif (computer == "air"):
            print("user win")


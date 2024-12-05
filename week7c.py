menu = {"ayamr":3.0 ,"fries":3.0, "chicken tenders":3.0, "nugget":3.0, "bakso":3.0, "water":3.0}

cusorder=[]
while(True):
    user = input("Wwhat u want to eat")

    if(user == 'n'):
        break
    cusorder.append(user)

print(cusorder)
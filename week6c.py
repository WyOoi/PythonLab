class BERR:
    def __init__(self,name,age,gender,subject1,score1,subject2,score2):
        self.n = name
        self.a = age
        self.g = gender
        self.s1 = subject1
        self.s2 = subject2
        self.sc1 = score1
        self.sc2 = score2

    def printdata(self):
        print("student name:", self.n)
        print("age: ", self.a)
        print("Gender: ",self.g)

    def calcgrade1(self):
        if self.sc1 >= 0 and self.sc1 <= 50:
            print("subject: ",self.s1)
            print("grade C")
        elif self.sc1 >= 51 and self.sc1 <= 80:
            print("subject: ",self.s1)
            print("grade b")
        elif self.sc1 >= 81 and self.sc1 <= 100:
            print("subject: ",self.s1)
            print("grade a")
        else:
            print("error")

    def calcgrade2(self):
        if self.sc2 >= 0 and self.sc2 <= 50:
            print("subject: ",self.s2)
            print("grade C")
        elif self.sc2 >= 51 and self.sc2 <= 80:
            print("subject: ",self.s2)
            print("grade b")
        elif self.sc2 >= 81 and self.sc2 <= 100:
            print("subject: ",self.s2)
            print("grade a")
        else:
            print("error")

s1 = BERR("ali",20,"male","AK2",100,"emt",90)
s2 = BERR("john",22,"male","AK2",200,"emt",40)

s1.printdata()
s1.calcgrade1()
s2.printdata()
s2.calcgrade2()
class Father:
    def skill1(self):
        print("Father: Driving")


class Mother:
    def skill2(self):
        print("Mother: Cooking")


class Child(Father, Mother):
    def skill3(self):
        print("Child: Programming")


child = Child()

child.skill1()
child.skill2()
child.skill3()
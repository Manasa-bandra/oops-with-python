class Student:
    def __init__(self, name, branch):
        self.name = name
        self.branch = branch

    def display(self):
        print(self.name, "-", self.branch)


s1 = Student("sindhu", "AIML")
s2 = Student("akhil", "CSE")
s3 = Student("siri", "ECE")

s1.display()
s2.display()
s3.display()
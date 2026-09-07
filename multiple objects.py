class sample:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def read(self):
        print(self.name)
        print(self.age)

# Creating objects and calling methods
s1 = sample("kpnt", 20)
s1.read()

s2 = sample("abc", 2)
s2.read()
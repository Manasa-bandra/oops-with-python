class Grandparent:
    def property(self):
        print("Grandparent has property")


class Parent(Grandparent):
    def house(self):
        print("Parent has a house")


class Child(Parent):
    def education(self):
        print("Child is studying")


child = Child()

child.property()
child.house()
child.education()
class Person:
    def __init__(self,age,name):
        self.age =age
        self.name = name

    def greet(self):
        print("parent class")


class Employee(Person):
    def __init__(self, des, id):
        Person.__init__(self,age=20, name = "asif")
        self.des = des
        self.id = id
    def greet(self):
        print("dervied class")


e = Employee("developer",40)
e.greet()
class Employee:
    def __init__(self,name):
        self.name = name

    def detail(self):
        print(f"the Employee is {self.name}")

class coder:
    def __init__(self,lang):
        self.lang =lang

    def detail(self):
        print(f"printing the language {self.lang}")

class programmer(Employee,coder):
    def __init__(self, name,lang):
        self.lang =lang
        self.name =name

p = programmer("c#","zaid")
print(p.name)
print(p.lang)
print(p.detail())
print(programmer.mro())

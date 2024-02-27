class Employee:
    def __init__(self,name):
        self.name = name

class coder:
    def __init__(self,lang):
        self.lang =lang


class programmer(Employee,coder):
    def __init__(self, name,lang):
        self.lang =lang
        self.name =name

p = programmer("c#","zaid")
print(p.name)
print(p.lang)

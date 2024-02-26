class Person:
    def __init__(self):
        self._name = "amir"

    def _greet(self):
        return "semester 7th"
    
class Student(Person):
    pass

s1 = Person()
s2 = Student()
print(s1._name)
print(s1._greet())
print(s2._name)
print(s2._greet())
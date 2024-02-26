class Student:
    def __init__(self):
        print("base")

    def greet(self):
        print(f'Good Morning ')

class miniStudent (Student):

    def __init__(self):
        Student.__init__(self)
        
    def display(self):
        print("Child class")    
    
    def greet(self):
        Student.greet(self)
        print("base class greet")

class passStudent(Student):
    pass #for ignoring the data in it , it will call the methods of the parent class

s = miniStudent()
s.greet()
s.display()
class Person:
    def __init__(self,age,name):
        self.__age = age
        self.__name = name


p = Person(80,"asif")
print(p._Person__name) # works for private values
print(p.__dir__())
#print(p.__age) #private error

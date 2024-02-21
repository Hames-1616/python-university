class student:

    def __init__(self,name,roll):
        self.name= name,
        self.roll = roll

    def __str__(self):
        print(self.name)

s = student("amir",90)
s.__str__()
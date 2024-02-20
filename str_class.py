class student:

    def __init__(self,name,roll):
        self.name= name,
        self.roll = roll

    def __str__(self):
        return f"{self.name} ({self.roll})"

s = student("amir",90)
print(s.__str__())

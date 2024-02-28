class Paris:
    def func1(self):
        print("Paris")

class Japan(Paris):
    def func2(self):
        print("Japan")

class Berlin(Paris):
    def func3(self):
        print("Berlin")

class Tokyo(Paris,Japan):
    
class Manager:
    def review(self):
        print("final review")

class tester(Manager):
    def review(self):
        print("testing")

class coder(tester):
    def writes(self):
        print("writing code")


w = coder()

w.review()
w.writes()
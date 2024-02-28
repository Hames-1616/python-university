def outer(x):
    def inner(y):
        return x+y
    return inner


def greet(fx):
    def fx1():
        print("welcome")
        fx()
        print("thanks")
        return fx1

@greet
#decorators
def Iust():
    print("hey there")


i = Iust()

o = outer(7)
z= o(3)
print(z)

# a decorator is a fnx that takes another fnx as an argument and returns a new function that modifies the behaviour of the original function the new Function is often refered to as decorated function
### and syntax is @decoratior.fxn





from multi_dispatch import dispatch

class opt:
    @dispatch(int)
    def fxn(x):
        print("integer function")

    @dispatch(float)
    def fxn(x):
        print("float ifunction")


o = opt()
o.fxn(12)
o.fxn(12.2)

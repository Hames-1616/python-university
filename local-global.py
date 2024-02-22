# global and local variable
y=10

print(y)

def cal():
    global y # for changing the value globally
    y = 20
    print(y)

cal()
print(y)
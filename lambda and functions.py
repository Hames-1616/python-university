import functools
def square(x):
    return x * x
print(square(3))

l = [3,4,5,6,7,8]
l1 = []
for i in l:
    l1.append(square(i))

l1 = list(map(square,l))
print(l1)

#reduce(fxn,iterable)

l2 = list(filter(square,l))
print(l2)

l3 = list(map(lambda x : x*x,l))

s = functools.reduce(lambda x,y:x+y,l)
print(s)

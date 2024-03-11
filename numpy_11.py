import numpy as np

s = np.zeros((3,4))
x = np.ones((2,3))
f = np.arrange(0,10,2)
a = np.random.rand(2,3)

print(x.shape)
print(x.dtype)
print(x.size)
print(x.reshape((3,2)))

p = np.array([4,5,3,2])
q = np.array([7,8,9,5])
t = p+q
u = p-q
v = p*q
b= p/q
print(np.mean(p))
print(np.median(p))
print(np.mode(p))
np.add(p,q)
np.sub(p,q)
np.matmul(p,q)
np.divide(p,q)
np.sqrt(p)
p.ravel()

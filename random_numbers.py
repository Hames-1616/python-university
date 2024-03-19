from numpy import random
import numpy as np
x=random.randint(100)
print(x)
print(random.rand()) #float between 0 and 1
print(random.randint(100,size=5))
print(random.randint(100,size=(3,4)))

#float -> rand(5)
print(random.rand(5))
print(random.rand(3,5))

print(random.choice([8,7,4,2,1])) # chosing value from the list

print(random.choice([8,7,4,2,3],size=(5,3)))


#generate a 1d array containing 50 values where values and probablity are as follows 0-1 0 means no occurence and 1 means 100% chance of occurence
# value     probablity
# 8         0.3
# 7         0.1
# 5         0.4
# 3         0.1
# 4         0.1
# 2         0.0
# total     1.0
print("printing the answer")
s = random.choice([8,7,5,3,4,2],p=[0.3,0.1,0.4,0.1,0.0,0.1],size=(5,3))
print(s)

#random permutation
# shuffle   and     permutation

a = np.array([4,3,2,9,7])
random.shuffle(a) # shuffle changes the contents of a
print(a)
r = random.permutation(a)
random.shuffle(r)
print(r)
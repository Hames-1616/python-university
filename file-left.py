f = open("try.txt","r")
print(f.read())
# t = f.read() cannot use this in write mode 
t = f.readline()

while True:
    t = f.readline()
    print(t)

    if not t:
        break
    L1 = t.split(",")[0]
    L2 = t.split(",")[1]
    L3 = t.split(",")[2]

    print(L1)
    print(L2)
    print(L3)

# in dis way we dont need to close the file 
with open("try.txt","r") as f:
    s = f.read()
    s=s.replace("\n",",")
    ls = s.split(",")
    print(ls)
    print(f.read())





f.close()
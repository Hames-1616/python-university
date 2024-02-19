f = open("notes.txt")
# or we can set open("notes.txt","rt")
print(f.read())
print(f.read(10)) # reads 10 characters
print(f.readline()) # reads lines
print(f.readline())
for x in f :
    print(x)
f.close()

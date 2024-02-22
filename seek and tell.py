with open("try.txt") as f:
    f.seek(2)
    t = f.read()
    print(t)
    print(f.tell())
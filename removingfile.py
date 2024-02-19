from os import remove,path

remove("operations.txt") #deletes file and if the file doesnt exists it shows an error

if path.exists("operations.txt"):
    remove("operations.txt")
else:
    print("file doesnt exsts")
import pandas as p

#series

a = [3,7,5]
s = p.Series(a,index=["a","b","c"])
print(s)

# data frames
python = {
    "name":["asif","umar","akash"],
    "roll" : [3,9,5]
}
q = p.DataFrame(python)
print(q)
print(q.loc[1])
#print(q.loc[]) try with 2 values

t=p.DataFrame(python,index=["student1","student2","student3"])

print(t)
print(t.loc["student1"])


f=p.read_csv("present.csv")
print(f)
print(f.to_string)
print(f.head(5))
print(f.tail(5))
print(f.info())


#max rows
print(p.options.display.max_rows)


student = {
    "java":{
        11:"haamid"
    },
    "IOT" : {
        22:"hidayat",
        44:"Ruhail"
    }
}

print(p.DataFrame(student))
import pandas as pd

s = pd.read_csv('housing.csv')

t = s.dropna()
print(t.to_string)
p = s.fillna(50,inplace=True) #for replacing any empty value
s['bedrooms'].fillna("yes",inplace=True) ## for replacing the empty place in the column with yes
q = s['price'].mean()
print(q)
print(s['price'].median())
print(s['price'].mode())
print(s['price'].mode().values[0])
# pd.to_datetime() # for proper converting of datetimes
s['price'] =s['price'].astype(float)


pd.to_numeric(s['area'],errors='coerce')

s.loc[7,"area"] = 1 #replaces the data at 7 pos with 1


for x in s.index:
    if s.loc[x,"area"] > 100:
        s.loc[x,"area"] = 150 * x
        s.drop(x,inplace=True)

print(s.head(10))
print(s.corr())



# print(t.to_string)

import pandas as pd

s = pd.read_csv('housing.csv')
t = s.dropna()
print(t.to_string)
p = s.fillna(50,inplace=True) #for replacing any empty value
s['bedrooms'].fillna("yes",inplace=True) ## for replacing the empty place in the column with yes

# print(t.to_string)

import pandas as pd

df=pd.read_csv('enjoysport.csv')
data = list(df.values)

specific = data[0][:-1]
general = [['?' for i in range(len(specific))] for j in range(len(specific))]

for i in data:
    if i[-1] == "yes":
        for j in range(len(specific)):
            if i[j] != specific[j]:
                specific[j] = "?"
                general[j][j] = "?"

    elif i[-1] == "no":
        for j in range(len(specific)):
            if i[j] != specific[j]:
                general[j][j] = specific[j]
            else:
                general[j][j] = "?"
  
gh = [] 
for i in general:
    for j in i:
        if j != '?':
            gh.append(i)
            break
print("\nFinal Specific hypothesis:\n", specific)
print("\nFinal General hypothesis:\n", gh)

import pandas as pd
df = pd.read_csv('enjoysport.csv')
column_length = df.shape[1]

h = ['0'] * (column_length - 1)
hp = []
hn = []
for training_example in df.values:
    if training_example[-1] != 'no':
        hp.append(list(training_example))
    else:
        hn.append(list(training_example))

for i in range(len(hp)):
    for j in range(column_length - 1):
        if h[j] == '0':
            h[j] = hp[i][j]
        if h[j] != hp[i][j]:
            h[j] = '?'
print(f'Positive Hypotheses:\n{hp}')
print(f'Negative Hypotheses:\n{hn}')
print(f'Maximally Specific Hypotheses:\n{h}')

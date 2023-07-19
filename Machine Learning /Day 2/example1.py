import pandas as pd

df = pd.read_excel('data.xlsx')

mean = df.mean()
median = df.median()
mode = df.mode()

print('Mean:', mean)
print('Median:', median)
print('Mode:', mode)

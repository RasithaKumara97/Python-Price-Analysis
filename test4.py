import pandas

df = pandas.read_csv('E:\Kingslake\Tea Details.csv')
print(df)
print("--------------------------------")
print("Minimum Values")
print("--------------------------------")
print(df.groupby('Tea Brand').min().Prices)
print("--------------------------------")
print("Maximum Values")
print("--------------------------------")
print(df.groupby('Tea Brand').max().Prices)

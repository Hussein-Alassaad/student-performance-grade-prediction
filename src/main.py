import pandas as pd

df = pd.read_csv("Data/student_performance.csv", sep=";")

print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df["G3"].describe())



import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Data/student_performance.csv", sep=";")

print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df["G3"].describe())



plt.hist(df["G3"], bins=20)
plt.title("Distribution of Final Grades")
plt.xlabel("G3")
plt.ylabel("Number of Students")
plt.show()   



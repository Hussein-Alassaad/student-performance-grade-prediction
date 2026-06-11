import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Data/student_performance.csv", sep=";")

# print(df.head())
#print(df.shape)
#print(df.columns)
#print(df.info())
#print(df["G3"].describe())



#plt.hist(df["G3"], bins = 20 )
#plt.title("Distribution of Final Grades")
#plt.xlabel("G3")
#plt.ylabel("final grade")
#plt.show()




#plt.scatter(df["studytime"], df["G3"])

#plt.title("Study Time vs Final Grade")
#plt.xlabel("Study Time")
#plt.ylabel("Number of Students")
#plt.show()

#plt.scatter(df["G2"], df["G3"])


#plt.title("G2 vs Final Grade")
#plt.xlabel("G2")
#plt.ylabel("Final Grade (G3)")

#plt.show()


#plt.scatter(df["G1"], df["G3"])
#plt.title("G1 vs G3")
#plt.xlabel("G1")
#plt.ylabel("G3")
#plt.show()

print(df.corr(numeric_only=True)["G3"].sort_values(ascending=False))

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score

x = df[["G1" , "G2"]]
y = df["G3"]
#print(x.head())
#print(y.head())

X_train, X_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)

print("Training features shape:", X_train.shape)
print("Testing features shape:", X_test.shape)
print("Training target shape:", y_train.shape)
print("Testing target shape:", y_test.shape)

ml = LinearRegression() # create the model 

ml.fit(X_train, y_train)

y_pred = ml.predict(X_test)
print(y_pred[:5])

print(y_test[:5])
print(y_pred[:5])

mae = mean_absolute_error(y_test, y_pred)
print(mae)

r2 = r2_score(y_test, y_pred)
print(r2)







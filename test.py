from sklearn import datasets
import pandas as pd

iris = datasets.load_iris()
print(type(iris))
print(iris.keys())
print(type(iris.data), type(iris.target))
print(iris.data.shape)
print(iris.target_names)
X = iris.data
Y = iris.target
df = pd.DataFrame(X, columns=iris.feature_names)

print(df.head())

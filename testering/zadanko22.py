import pandas as pd

url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
titanic = pd.read_csv(url)

threshhold = len(titanic) * 0.4
titanic_clean = titanic.dropna(axis=1, thresh=threshhold)

print(titanic['Age'].describe())
mediana = titanic['Age'].median()
titanic['Age'] = titanic['Age'].fillna(mediana)
print(titanic['Age'].describe())

dominanta = titanic['Embarked'].mode()[0]
titanic['Embarked'] = titanic['Embarked'].fillna(dominanta)

print(f"Liczba wierszy przed: {len(titanic)}")
titanic.dropna(inplace=True)
print(f"Liczba wierszy po: {len(titanic)}")

print(titanic.isnull().sum().sum())
print(titanic.shape)
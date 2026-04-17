import pandas as pd

url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
titanic = pd.read_csv(url)

titanic['FamilySize'] = titanic['SibSp'] + titanic['Parch'] + 1

titanic['IsAlone'] = 0
titanic.loc[titanic['FamilySize'] == 1, 'IsAlone'] = 1

bins = [0, 12, 18, 35, 60, 120]
labels = ['0-12', '13-18', '19-35', '36-60', '60+']
titanic['AgeGroup'] = pd.cut(titanic['Age'], bins=bins, labels=labels)

survived_rate = titanic.groupby('IsAlone')['Survived'].mean()

print(survived_rate)


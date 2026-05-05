import pandas as pd
from scipy import stats

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"

wine = pd.read_csv(url, sep=';')

wine['z_score'] = stats.zscore(wine['alcohol'])
print(wine['alcohol'].describe())

wine_cleaned = wine[wine['z_score'].abs() <= 3]
print(wine_cleaned['alcohol'].describe())

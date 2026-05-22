import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import SGDRegressor
from sklearn.metrics import accuracy_score, classification_report


df = sns.load_dataset('titanic')


features = ['pclass', 'sex', 'age', 'fare', 'sibsp', 'parch']

df['age'] = df['age'].fillna(df['age'].median())
df['fare'] = df['fare'].fillna(df['fare'].mean())
df['sex'] = df['sex'].map({'female': 1, 'male': 0})

X = df[features]
y = df['survived']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


sgd_model = SGDRegressor(
    max_iter=1000, 
    tol=1e-6, 
    eta0=0.001, 
    random_state=42)

sgd_model.fit(X_train_scaled, y_train)

raw_preds_train = sgd_model.predict(X_train_scaled)
raw_preds_test = sgd_model.predict(X_test_scaled)

preds_train = (raw_preds_train >= 0.5).astype(int)
preds_test = (raw_preds_test >= 0.5).astype(int)


print("--- WYNIKI MODELU SGDRegressor ---")
print(f"Dokładność na zbiorze treningowym: {accuracy_score(y_train, preds_train) * 100:.2f}%")
print(f"Dokładność na zbiorze testowym:     {accuracy_score(y_test, preds_test) * 100:.2f}%")

print("\nSzczegółowy raport klasyfikacji dla zbioru testowego:")
print(classification_report(y_test, preds_test, target_names=['Zginął', 'Przeżył']))
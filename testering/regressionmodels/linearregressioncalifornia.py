import pandas as pd
import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score


california = fetch_california_housing(as_frame=True)
df = california.frame

X = california.data
y = california.target  

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


model = LinearRegression()
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)


mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("--- Wyniki modelu Regresji Liniowej ---")

print(f"Średni błąd bezwzględny (MAE): ${mae * 100000:.2f}")
print(f"Współczynnik dopasowania R2: {r2 * 100:.2f}%")


print("\nWpływ poszczególnych cech na cenę domu (od najważniejszej):")
coefficients = pd.DataFrame({
    'Cecha': california.feature_names,
    'Waga (Współczynnik)': model.coef_
})

coefficients['Abs_Waga'] = coefficients['Waga (Współczynnik)'].abs()
coefficients = coefficients.sort_values(by='Abs_Waga', ascending=False).drop(columns=['Abs_Waga'])
print(coefficients.to_string(index=False))
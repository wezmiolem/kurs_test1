import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score


california = fetch_california_housing(as_frame=True)
X = california.data
y = california.target  


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)

print("Trenowanie Lasu Losowego... Proszę chwilę poczekać.")
model.fit(X_train, y_train)


y_pred = model.predict(X_test)


mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n--- WYNIKI MODELU RANDOM FOREST ---")
print(f"Średni błąd bezwzględny (MAE): ${mae * 100000:.2f}")
print(f"Współczynnik dopasowania (R2 Score): {r2 * 100:.2f}%")

importances = model.feature_importances_

feature_importance_df = pd.DataFrame({
    'Cecha': california.feature_names,
    'Istotność (Wpływ)': importances
})

# Sortujemy wyniki od najważniejszej cechy
feature_importance_df = feature_importance_df.sort_values(by='Istotność (Wpływ)', ascending=False)

print("\n--- WAŻNOŚĆ CECH W RANDOM FOREST ---")
for index, row in feature_importance_df.iterrows():
    print(f"{row['Cecha']}: {row['Istotność (Wpływ)'] * 100:.2f}%")
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import SGDRegressor
from sklearn.metrics import mean_absolute_error, r2_score


california = fetch_california_housing(as_frame=True)
X = california.data
y = california.target


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


model_sgd = SGDRegressor(
    loss='squared_error',      
    learning_rate='constant',  
    eta0=0.00001,                
    max_iter=3000,            
    tol=1e-6,                  
    random_state=42
)

print("Trenowanie regresji za pomocą Spadku Gradientu...")
model_sgd.fit(X_train_scaled, y_train)


y_pred = model_sgd.predict(X_test_scaled)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n--- WYNIKI REGRESJI SGD ---")
print(f"Średni błąd bezwzględny (MAE): ${mae * 100000:.2f}")
print(f"Współczynnik dopasowania (R2 Score): {r2 * 100:.2f}%")
print(f"Liczba faktycznie wykonanych iteracji: {model_sgd.n_iter_}")
import pandas as pd
import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score, classification_report


digits = load_digits()
X, y = digits.data, digits.target


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


model_sgd = SGDClassifier(
    loss='log_loss',           # 'log_loss' - regresja logistyczna
    learning_rate='constant',  # 'optimal' 'invscaling' 'adaptive'
    eta0=0.0001,               #  LEARNING RATE
    max_iter=2000,             #  maksymalna liczba epok (podejść do danych)
    tol=1e-3,                  #  margines spadku bledu
    random_state=42
)

print("Trenowanie klasyfikatora SGD przy użyciu Spadku Gradientu...")
model_sgd.fit(X_train_scaled, y_train)

y_pred = model_sgd.predict(X_test_scaled)

accuracy = accuracy_score(y_test, y_pred)
print("\n--- WYNIKI KLASYFIKACJI SGD ---")
print(f"Ogólna dokładność (Accuracy): {accuracy * 100:.2f}%")
print(f"Liczba faktycznie wykonanych kroków (epok): {model_sgd.n_iter_}")

print("\nSzczegółowy raport dla każdej cyfry:")
print(classification_report(y_test, y_pred))
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

digits = load_digits()
X = digits.data  
y = digits.target 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=10000)

print("Trenowanie modelu... Może to chwilę potrwać.")
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print("\n--- Podsumowanie ---")
print(f"Ogólna dokładność (Accuracy): {accuracy * 100:.2f}%")
print("\nSzczegółowy raport dla każdej cyfry:")
print(classification_report(y_test, y_pred))
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score

data = load_breast_cancer()
X, y = data.data, data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = LogisticRegression(max_iter=10000)
model.fit(X_train, y_train)

y_probs = model.predict_proba(X_test)[:, 1]

thresholds = np.arange(0.1, 0.95, 0.05)
f1_scores = []

for threshold in thresholds:
    y_pred = (y_probs >= threshold).astype(int)
    score = f1_score(y_test, y_pred)
    f1_scores.append(score)

# Wskazanie optymalnego progu
best_index = np.argmax(f1_scores)
best_threshold = thresholds[best_index]
best_f1 = f1_scores[best_index]

print(f"Optymalny próg decyzyjny: {best_threshold:.2f}")
print(f"Maksymalny F1-score: {best_f1:.4f}")

# Wizualizacja zależności próg -> F1
plt.figure(figsize=(10, 6))
plt.plot(thresholds, f1_scores, marker='o', linestyle='-', color='b')
plt.axvline(best_threshold, color='r', linestyle='--', label=f'Optymalny próg ({best_threshold:.2f})')
plt.title('Zależność F1-score od progu decyzyjnego')
plt.xlabel('Próg (Threshold)')
plt.ylabel('F1-score')
plt.xticks(np.arange(0.1, 1.0, 0.1))
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()
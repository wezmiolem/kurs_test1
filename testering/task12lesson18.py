import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import learning_curve


digits = load_digits()
X, y = digits.data, digits.target

models = {
    "Decision Tree (Overfitting)": DecisionTreeClassifier(max_depth=None),
    "Random Forest (Balanced)": RandomForestClassifier(n_estimators=50, max_depth=5)
}

def plot_learning_curve(estimator, title, X, y, ax):
    train_sizes, train_scores, test_scores = learning_curve(
        estimator, X, y, cv=5, n_jobs=-1, 
        train_sizes=np.linspace(0.1, 1.0, 10), scoring='accuracy'
    )
    
    train_mean = np.mean(train_scores, axis=1)
    test_mean = np.mean(test_scores, axis=1)

    ax.plot(train_sizes, train_mean, 'o-', color="r", label="Training score")
    ax.plot(train_sizes, test_mean, 'o-', color="g", label="Cross-validation score")
    ax.set_title(title)
    ax.set_xlabel("Training examples")
    ax.set_ylabel("Score (Accuracy)")
    ax.legend(loc="best")
    ax.grid(True)


fig, axes = plt.subplots(1, 2, figsize=(15, 5))

for ax, (name, model) in zip(axes, models.items()):
    plot_learning_curve(model, name, X, y, ax)

plt.tight_layout()
plt.show()
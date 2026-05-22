import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
from imblearn.under_sampling import RandomUnderSampler


X, y = make_classification(
    n_samples=1000, 
    n_features=20, 
    weights=[0.9, 0.1], 
    random_state=42
)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

results = {}

#  Bez korekcji 
model_raw = LogisticRegression()
model_raw.fit(X_train, y_train)
y_pred_raw = model_raw.predict(X_test)
results['Bez korekcji'] = f1_score(y_test, y_pred_raw)

#  class_weight='balanced' 
model_balanced = LogisticRegression(class_weight='balanced')
model_balanced.fit(X_train, y_train)
y_pred_balanced = model_balanced.predict(X_test)
results['Class Weight'] = f1_score(y_test, y_pred_balanced)

#  Undersampling
rus = RandomUnderSampler(random_state=42)
X_resampled, y_resampled = rus.fit_resample(X_train, y_train)
model_under = LogisticRegression()
model_under.fit(X_resampled, y_resampled)
y_pred_under = model_under.predict(X_test)
results['Undersampling'] = f1_score(y_test, y_pred_under)


plt.figure(figsize=(10, 6))
sns.barplot(x=list(results.keys()), y=list(results.values()), palette='viridis')
plt.title('Porównanie F1-score dla klasy mniejszościowej (10%)')
plt.ylabel('F1-score')
plt.ylim(0, 1)
for i, v in enumerate(results.values()):
    plt.text(i, v + 0.02, f'{v:.2f}', ha='center', fontweight='bold')
plt.show()
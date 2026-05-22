import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix


url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

df['Age'] = df['Age'].fillna(df['Age'].median())  
df['Fare'] = df['Fare'].fillna(df['Fare'].mean())
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1}) 


features = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare']
X = df[features]
y = df['Survived']

print(df.describe())
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression()
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)

y_proba = model.predict_proba(X_test_scaled)

print(f"Dokładność klasyfikacji (Accuracy): {accuracy_score(y_test, y_pred) * 100:.2f}%")
print("\nMacierz pomyłek (Confusion Matrix):")
print(confusion_matrix(y_test, y_pred))

print("\nSzczegółowy raport klasyfikacji:")
print(classification_report(y_test, y_pred, target_names=['Zmarł', 'Przeżył']))


print("\nPrawdopodobieństwo śmierci vs przeżycia:")
for i in range(5):
    print(f"Pasażer {i+1}: Śmierć: {y_proba[i][0]:.2f}, Przeżycie: {y_proba[i][1]:.2f} -> Wybór: {y_pred[i]}")
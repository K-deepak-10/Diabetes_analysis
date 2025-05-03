import pandas as pd; import numpy as np; from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier; import matplotlib.pyplot as plt
import seaborn as sns

# Load and clean data
df = pd.read_csv("diabetes.csv")
invalid_cols = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
df[invalid_cols] = df[invalid_cols].replace(0, np.nan)
df.fillna(df.median(), inplace=True)

# Split features and target
X = df.drop("Outcome", axis=1)
y = df["Outcome"]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Random Forest model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Feature importance
importances = pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False)
print("Feature Importances:\n", importances)

# Plot feature importance
plt.figure(figsize=(8, 5))
sns.barplot(x=importances.values, y=importances.index, palette="viridis")
plt.title("Key Indicators Contributing to Diabetes")
plt.xlabel("Importance Score")
plt.ylabel("Feature")
plt.show()

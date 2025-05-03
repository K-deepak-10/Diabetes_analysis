import pandas as pd; import numpy as np; import seaborn as sns; import matplotlib.pyplot as plt

# Load dataset and display basic info
df = pd.read_csv("diabetes.csv"); print(df.head()); print(df.info()); print(df.isnull().sum())

# Descriptive statistics and outcome distribution
print(df.describe()); print("Outcome count:\n", df['Outcome'].value_counts())

# Identify invalid zeros
invalid_cols = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
for col in invalid_cols: print(f"{col} has {(df[col]==0).sum()} zero values")

# Replace zeros with NaN and fill with median
df[invalid_cols] = df[invalid_cols].replace(0, np.nan); df.fillna(df.median(), inplace=True)

# Correlation heatmap
plt.figure(figsize=(10, 6)); sns.heatmap(df.corr(), annot=True, cmap="coolwarm"); plt.title("Correlation Heatmap"); plt.show()

# Histograms of key features by diabetes outcome
for col in ['Glucose', 'BMI', 'Age', 'Pregnancies']: 
    plt.figure(figsize=(6, 4)); sns.histplot(data=df, x=col, hue='Outcome', kde=True, bins=30); 
    plt.title(f'{col} Distribution by Outcome'); plt.show()

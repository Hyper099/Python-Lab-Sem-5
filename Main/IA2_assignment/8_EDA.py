import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
columns = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 
           'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target']

df = pd.read_csv('./Data/heart+disease/processed.cleveland.data', 
                 names=columns, na_values='?')

print("=== HEART DISEASE EDA ===\n")

# 1. Data Overview
print("1. DATASET SHAPE:", df.shape)
print("\nFirst 3 rows:")
print(df.head(3))

# 2. Data Preprocessing
print("\n2. MISSING VALUES:")
print(df.isnull().sum()[df.isnull().sum() > 0])

# Fill missing values
df.fillna(df.median(), inplace=True)

# Convert target to binary
df['target'] = df['target'].apply(lambda x: 1 if x > 0 else 0)
print("\nTarget converted: 0=No Disease, 1=Disease")

# 3. Basic Statistics
print("\n3. BASIC STATISTICS:")
print(df.describe())

# 4. Target Distribution
print("\n4. TARGET DISTRIBUTION:")
print(df['target'].value_counts())
print(f"Disease rate: {df['target'].mean()*100:.1f}%")

# 5. Feature Correlation
print("\n5. CORRELATION WITH TARGET:")
corr = df.corr()['target'].sort_values(ascending=False)
print(corr)

# 6. Key Insights
print("\n6. KEY INSIGHTS:")
print(f"- Mean age: {df['age'].mean():.1f} years")
print(f"- Male patients: {(df['sex']==1).sum()} ({(df['sex']==1).sum()/len(df)*100:.1f}%)")
print(f"- Disease in males: {df[df['sex']==1]['target'].mean()*100:.1f}%")
print(f"- Disease in females: {df[df['sex']==0]['target'].mean()*100:.1f}%")

# 7. Visualizations
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Target distribution
df['target'].value_counts().plot(kind='bar', ax=axes[0,0], color=['green', 'red'])
axes[0,0].set_title('Disease Distribution')
axes[0,0].set_xlabel('0=No Disease, 1=Disease')

# Age distribution
df['age'].hist(bins=20, ax=axes[0,1], color='skyblue', edgecolor='black')
axes[0,1].set_title('Age Distribution')
axes[0,1].set_xlabel('Age')

# Correlation heatmap
sns.heatmap(corr.to_frame(), annot=True, cmap='coolwarm', ax=axes[1,0])
axes[1,0].set_title('Correlation with Target')

# Sex vs Disease
pd.crosstab(df['sex'], df['target']).plot(kind='bar', ax=axes[1,1], color=['green', 'red'])
axes[1,1].set_title('Sex vs Heart Disease')
axes[1,1].set_xlabel('Sex (0=Female, 1=Male)')
axes[1,1].legend(['No Disease', 'Disease'])

plt.tight_layout()
plt.savefig('./Main/IA2_assignment/heart_eda.png', dpi=150)
print("\n✓ Visualization saved as 'heart_eda.png'")
plt.show()

print("\n=== EDA COMPLETE ===")

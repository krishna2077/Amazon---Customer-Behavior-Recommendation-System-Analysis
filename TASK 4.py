
# Recommendation and Review Insights
#-------------------------- SUBTASK 1 -----------------------------------------
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import spearmanr

# Loading the dataset
df = pd.read_csv('D:\Course Data DS\Amazon_numeric_fixed.csv')

# Map Recommendation Helpfulness to an ordinal scale
mapping = {'No': 1, 'Sometimes': 2, 'Yes': 3}
df['Helpfulness_Score'] = df['Recommendation_Helpfulness'].map(mapping)

# Calculate Correlation
correlation, p_val = spearmanr(df['Helpfulness_Score'], df['Shopping_Satisfaction'])
print(f"Correlation: {correlation:.3f}")

# Visualization: Satisfaction by Helpfulness Category
sns.boxplot(x='Recommendation_Helpfulness', y='Shopping_Satisfaction', data=df, 
            order=['No', 'Sometimes', 'Yes'], palette='vlag')
plt.title('Impact of Recommendations on Shopping Satisfaction')
plt.xlabel('Recommendation Helpfulness')
plt.ylabel('Satisfaction (1-5)')
plt.savefig('helpfulness_vs_satisfaction.png')

#-------------------------- SUBTASK 2 -----------------------------------------
import pandas as pd
from scipy.stats import spearmanr

# Loading the dataset
df = pd.read_csv('D:\Course Data DS\Amazon_numeric_fixed.csv')

# Map categories to numeric scales
rel_map = {'Heavily': 5, 'Moderately': 4, 'Occasionally': 3, 'Rarely': 2, 'Never': 1}
help_map = {'Yes': 3, 'Sometimes': 2, 'No': 1}

df['Rel_Score'] = df['Review_Reliability'].map(rel_map)
df['Help_Score'] = df['Review_Helpfulness'].map(help_map)

# Grouped analysis for Reliability
reliability_summary = df.groupby('Review_Reliability')[['Rating_Accuracy', 'Shopping_Satisfaction']].mean()
print(reliability_summary)

# Correlation (Spearman)
corr, p_val = spearmanr(df['Rel_Score'], df['Rating_Accuracy'])
print(f"Reliability vs Accuracy Correlation: {corr:.3f}")

#-------------------------- SUBTASK 3 -----------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('D:\Course Data DS\Amazon_numeric_fixed.csv')

# 1. Frequency of Personalized Recommendations
rec_freq_counts = df['Personalized_Recommendation_Frequency'].value_counts()

# 2. Trust/Helpfulness of Recommendations
rec_help_counts = df['Recommendation_Helpfulness'].value_counts()

# 3. Visualization
fig, ax = plt.subplots(1, 2, figsize=(16, 6))

# Pie Chart for Exposure
rec_freq_counts.plot(kind='pie', ax=ax[0], autopct='%1.1f%%', colors=sns.color_palette('pastel'))
ax[0].set_title('Exposure to Recommendations')

# Bar Chart for Helpfulness
rec_help_counts.plot(kind='bar', ax=ax[1], color='teal')
ax[1].set_title('Trust: Perceived Helpfulness')

plt.savefig('recommendation_trends.png')



















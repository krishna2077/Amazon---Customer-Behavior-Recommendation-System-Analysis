
# Visualization and Reporting
#-------------------------- SUBTASK 1 -----------------------------------------
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Loading data
df = pd.read_csv('D:\Course Data DS\Amazon_numeric_fixed.csv')

# Purchase Categories Bar Chart
all_categories = df['Purchase_Categories'].str.split(';').explode().str.strip()
sns.barplot(x=all_categories.value_counts().values, y=all_categories.value_counts().index, palette='viridis')
plt.title('Distribution of Purchase Categories')
plt.savefig('purchase_categories_bar.png')

# Browsing Frequency Pie Chart
df['Browsing_Frequency'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=sns.color_palette('pastel'))
plt.title('Browsing Frequency Distribution')
plt.savefig('browsing_frequency_pie.png')

# Satisfaction Levels Bar Chart
sns.barplot(x=df['Shopping_Satisfaction'].value_counts().index, y=df['Shopping_Satisfaction'].value_counts().values)
plt.title('Shopping Satisfaction Levels')
plt.savefig('satisfaction_levels_bar.png')

# Correlation Heatmap
corr_data = df[['Recommendation_Helpfulness_numeric', 'Shopping_Satisfaction']].corr(method='spearman')
sns.heatmap(corr_data, annot=True, cmap='RdBu', center=0)
plt.title('Correlation: Recommendation Usefulness & Satisfaction')
plt.savefig('recommendation_satisfaction_heatmap.png')




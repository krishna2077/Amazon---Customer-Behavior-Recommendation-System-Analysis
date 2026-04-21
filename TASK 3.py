

# Customer Segmentation and Profiling 
#-------------------------- SUBTASK 1 -----------------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Loading the data
df = pd.read_csv('D:\Course Data DS\Amazon_numeric_fixed.csv')

# Map Purchase_Frequency to a numeric scale (1-5)
freq_map = {
    'Multiple times a week': 5, 'Once a week': 4, 
    'Few times a month': 3, 'Once a month': 2, 'Less than once a month': 1
}
df['Freq_Score'] = df['Purchase_Frequency'].map(freq_map)

# Defining  segments using a 2x2 logic (Split at 3.5)
def segment_customer(row):
    f, s = row['Freq_Score'], row['Shopping_Satisfaction']
    if f >= 4 and s >= 4: return 'Champions'
    if f >= 4 and s < 4:  return 'Frustrated Regulars'
    if f < 4 and s >= 4:  return 'Satisfied Casuals'
    return 'At Risk / Disengaged'

df['Segment'] = df.apply(segment_customer, axis=1)

# Visualizing the segments
plt.figure(figsize=(10, 6))
sns.stripplot(data=df, x='Freq_Score', y='Shopping_Satisfaction', hue='Segment', jitter=0.25)
plt.axvline(3.5, color='gray', linestyle='--')
plt.axhline(3.5, color='gray', linestyle='--')
plt.title('Customer Segmentation: Frequency vs. Satisfaction')
plt.xlabel('Purchase Frequency (1: Low -> 5: High)')
plt.ylabel('Satisfaction (1: Low -> 5: High)')
plt.savefig('customer_segmentation.png')


#-------------------------- SUBTASK 3 -----------------------------------------
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Loading segmented data
df = pd.read_csv('D:\Course Data DS\Amazon_numeric_fixed.csv')

# Age Boxplot by Segment
sns.boxplot(data=df, x='Segment', y='age')
plt.title('Age Distribution Across Segments')
plt.savefig('age_by_segment.png')

# Gender Composition per Segment
gender_segment = pd.crosstab(df['Segment'], df['Gender'], normalize='index') * 100
gender_segment.plot(kind='bar', stacked=True)
plt.title('Gender Composition per Segment (%)')
plt.savefig('gender_by_segment.png')

# Browsing Frequency Comparison
browsing_segment = pd.crosstab(df['Segment'], df['Browsing_Frequency'], normalize='index') * 100
browsing_segment.plot(kind='bar', stacked=True)
plt.title('Browsing Frequency per Segment (%)')
plt.savefig('browsing_by_segment.png')

#-------------------------- SUBTASK 4 -----------------------------------------
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# Preparing features and scale
# (Includes Age, Frequencies, Review Importance, Satisfaction, etc.)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(scaler)

# Fit K-Means
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(X_scaled)

# Visualize using PCA (Principal Component Analysis)
pca = PCA(n_components=2)
pca_res = pca.fit_transform(X_scaled)
plt.scatter(pca_res[:, 0], pca_res[:, 1], c=clusters, cmap='Set1')
plt.title('Customer Behavioral Clusters')
plt.savefig('behavior_clusters.png')














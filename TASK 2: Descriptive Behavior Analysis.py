
# Descriptive Behavior Analysis 
#-------------------------- SUBTASK 1 -----------------------------------------
import pandas as pd
import matplotlib.pyplot as plt

# Loading the cleaned dataset
df = pd.read_csv('D:\Course Data DS\Amazon_numeric_fixed.csv')

# Age Summary
print("Age Statistics:")
print(df['age'].describe())

# Plotting Age Distribution
plt.hist(df['age'], bins=15, color='skyblue', edgecolor='black')
plt.title('Distribution of Customer Age')
plt.xlabel('Age')
plt.ylabel('Number of Customers')
plt.savefig('age_distribution.png')
plt.close()

# Gender Distribution
gender_counts = df['Gender'].value_counts()
print("\nGender Distribution:")
print(gender_counts)

# Plotting Gender Distribution (Sorted)
gender_counts.sort_values(ascending=False).plot(kind='bar', color='salmon')
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('gender_distribution.png')
plt.close()


#-------------------------- SUBTASK 2 -----------------------------------------
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('D:\Course Data DS\Amazon_numeric_fixed.csv')

# Purchase Frequency Analysis
purchase_freq_counts = df['Purchase_Frequency'].value_counts()

# Plotting Purchase Frequency
purchase_freq_counts.sort_values(ascending=False).plot(kind='bar', color='skyblue')
plt.title('Overall Purchase Frequency')
plt.xlabel('Frequency')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('purchase_frequency.png')
plt.close()

# Product Category Analysis
all_categories = df['Purchase_Categories'].str.split(';').explode().str.strip()
category_counts = all_categories.value_counts()

# Plotting Popular Categories
category_counts.sort_values(ascending=False).plot(kind='bar', color='lightgreen')
plt.title('Most Popular Product Categories')
plt.xlabel('Category')
plt.ylabel('Number of Mentions')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('popular_categories.png')
plt.close()


#-------------------------- SUBTASK 3 -----------------------------------------
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('D:\Course Data DS\Amazon_numeric_fixed.csv')

# Product Search Method Analysis
# Splitting and expanding in case of multiple selections
search_methods = df['Product_Search_Method'].str.split(';').explode().str.strip()
search_method_counts = search_methods.value_counts()

# Plotting Top Search Methods
search_method_counts.sort_values(ascending=False).plot(kind='bar', color='skyblue')
plt.title('Top Product Search Methods')
plt.xlabel('Search Method')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('search_methods.png')
plt.close()

# Cart Abandonment Factor Analysis
# Splitting and expanding for multi-select responses
abandonment_factors = df['Cart_Abandonment_Factors'].str.split(';').explode().str.strip()
abandonment_counts = abandonment_factors.value_counts()

# Plotting Abandonment Factors
abandonment_counts.sort_values(ascending=False).plot(kind='bar', color='coral')
plt.title('Common Cart Abandonment Factors')
plt.xlabel('Factor')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('abandonment_factors.png')
plt.close()


#-------------------------- SUBTASK 4 -----------------------------------------
import pandas as pd

# Loading the dataset
df = pd.read_csv('D:\Course Data DS\Amazon_numeric_fixed.csv')

# Map Recommendation_Helpfulness for numerical analysis
# (No=1, Sometimes=2, Yes=3)
helpfulness_mapping = {'No': 1, 'Sometimes': 2, 'Yes': 3}
df['Helpfulness_Score'] = df['Recommendation_Helpfulness'].map(helpfulness_mapping)

# Select target columns
targets = {
    'Shopping_Satisfaction': df['Shopping_Satisfaction'],
    'Rating_Accuracy': df['Rating_Accuracy'],
    'Recommendation_Helpfulness': df['Helpfulness_Score']
}

# Calculate and display metrics
print("--- Survey Sentiment Summary ---")
for name, data in targets.items():
    print(f"{name}:")
    print(f"  - Mean:   {data.mean():.2f}")
    print(f"  - Median: {data.median():.2f}")
    
    
#-------------------------- SUBTASK 5 -----------------------------------------
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('D:\Course Data DS\Amazon_numeric_fixed.csv')

# Defining variables to analyze
behavioral_vars = [
    'Purchase_Frequency', 'Browsing_Frequency', 
    'Search_Result_Exploration', 'Cart_Completion_Frequency', 'Review_Left'
]

# Generating counts and plots
for var in behavioral_vars:
    counts = df[var].value_counts()
    
    # Creating the visualization
    plt.figure(figsize=(10, 5))
    counts.sort_values(ascending=False).plot(kind='bar', color='teal')
    plt.title(f'Distribution of {var.replace("_", " ")}')
    plt.ylabel('Number of Responses')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig(f'behavior_{var}.png')
    plt.close()

# Printing top stats
    print(f"Top response for {var}: {counts.idxmax()} ({counts.max()} users)")
    

































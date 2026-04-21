# Data Cleaning and Preparation '''
#-------------------------- SUBTASK 1,2,3 -----------------------------------------
'''import pandas as pd

# Loading the dataset
df = pd.read_csv('D:\Course Data DS\Amazon.csv')
print(f"Original shape: {df.shape}")

# Cleaning Column Names
df.columns = df.columns.str.strip()

# Removing Exact Duplicates
df.drop_duplicates(inplace=True)
print(f"Shape after dropping exact duplicates: {df.shape}")

# Remove Duplicates by Unique ID
if 'transaction' in df.columns:
    df.drop_duplicates(subset=['transaction'], keep='last', inplace=True)
    print(f"Shape after dropping duplicate transactions: {df.shape}")

# Handle Inconsistent Responses (Logical Checks)
if 'age' in df.columns:
    # Convert to numeric, turning text errors into NaN
    df['age'] = pd.to_numeric(df['age'], errors='coerce') 
    # Keep only rows with valid ages
    df = df[(df['age'] >= 13) & (df['age'] <= 100)]
    print(f"Shape after filtering invalid ages: {df.shape}")

# Example B: Standardize Categorical Data (Text Case Inconsistencies)
if 'Gender' in df.columns:
    df['Gender'] = df['Gender'].str.title().str.strip()

# Handle Missing Values
critical_columns = ['Timestamp', 'Shopping_Satisfaction']
existing_critical = [col for col in critical_columns if col in df.columns]

if existing_critical:
    df.dropna(subset=existing_critical, inplace=True)
    print(f"Shape after dropping missing critical values: {df.shape}")

# Export the Cleaned Dataset
cleaned_filename = 'Amazon_cleaned.csv'
df.to_csv(cleaned_filename, index=False)
print(f"Cleaned dataset saved as: {cleaned_filename}")
'''
'''
#-------------------------- SUBTASK 4 -----------------------------------------
import pandas as pd
# Loading the dataset
df = pd.read_csv('D:\Course Data DS\PROJECT 6 FINALE\Amazon_cleaned.csv')

# Removing leading and trailing spaces from all column names
df.columns = df.columns.str.strip()

# Handling duplicate column names dynamically.
def deduplicate_columns(columns):
    counts = {}
    new_cols = []
    for col in columns:
        if col not in counts:
            counts[col] = 0
            new_cols.append(col)
        else:
            counts[col] += 1
            new_cols.append(f"{col}_{counts[col]}")
    return new_cols

df.columns = deduplicate_columns(df.columns)

# Exporting the fixed dataset
df.to_csv('Amazon_columns_fixed.csv', index=False)'''

#-------------------------- SUBTASK 5 -----------------------------------------
import pandas as pd
# Loading the dataset with fixed column names
df = pd.read_csv('D:\Course Data DS\PROJECT 6 FINALE\Amazon_cleaned.csv')

# List of columns to convert to numeric
numeric_cols = [
    'age', 
    'Customer_Reviews_Importance', 
    'Personalized_Recommendation_Frequency_1', 
    'Rating_Accuracy', 
    'Shopping_Satisfaction'
]

# Converting columns using pd.to_numeric
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Saving the updated dataset
df.to_csv('Amazon_numeric_fixed.csv', index=False)




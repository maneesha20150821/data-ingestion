import pandas as pd

# Load CSV
df = pd.read_csv("nsw_schools.csv")

# Preview first 5 rows
print(df.head())

# Column info (names, types, non-null counts)
print(df.info())

# Summary statistics (numeric + object columns)
print(df.describe(include="all"))

# Check missing values
print("Missing values per column:")
print(df.isnull().sum())

# Check percentage of missing values
print("Percentage of missing values per column:")
print((df.isnull().mean() * 100).round(2))

# Check duplicates
print(f"Number of duplicate rows: {df.duplicated().sum()}")

df['Indigenous_pct'] = pd.to_numeric(df['Indigenous_pct'], errors='coerce')
df['LBOTE_pct'] = pd.to_numeric(df['LBOTE_pct'], errors='coerce')
df.info()

# Drop completely empty column
df = df.drop(columns=["Support_classes"])
# Fill missing object columns with 'Unknown'
object_cols = df.select_dtypes(include="object").columns
df[object_cols] = df[object_cols].fillna("Unknown")
df.info()

print(df.head)

# Step 5: Create missing value indicator columns
missing_cols = ['ICSEA_value', 'FOEI_Value', 'latest_year_enrolment_FTE','Indigenous_pct','LBOTE_pct']
for col in missing_cols:
    df[f'{col}_missing'] = df[col].isnull().astype(int)

# Step 6: Save intermediate cleaned file
df.to_csv('nsw_schools_cleaned.csv', index=False)
print(df.columns)
print(df[['ICSEA_value_missing', 'FOEI_Value_missing', 'latest_year_enrolment_FTE_missing','Indigenous_pct_missing','LBOTE_pct_missing']].head(10))
for col in missing_cols:
    df[col] = df.groupby('LGA')[col].transform(lambda x: x.fillna(x.median()))

# Step 8: Save final cleaned dataset
df.to_csv('nsw_schools_final_cleaned.csv', index=False)
print(df.head(10))

# Step 9: Validate cleaning
print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nFinal preview:")
print(df.head())

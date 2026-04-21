import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("D:/Anmol_DMV_Lab/company_dataset.csv", nrows=50)

# Clean column names (safe)
df.columns = df.columns.str.strip()

# Data cleaning
df['ratings'] = pd.to_numeric(df['ratings'], errors='coerce')

df['review_count'] = df['review_count'].astype(str).str.replace(r'[^0-9]', '', regex=True)
df['review_count'] = pd.to_numeric(df['review_count'], errors='coerce')

df['years'] = df['years'].astype(str).str.extract(r'(\d+)').astype(float)

def convert_emp(x):
    if isinstance(x, str):
        if "Lakh+" in x: return 100000
        elif "50k-1" in x: return 75000
        elif "10k-50k" in x: return 30000
        elif "1k-5k" in x: return 3000
    return 0

df['emp_count'] = df['employees'].apply(convert_emp)

# 1. Top 10 HQ names
print(df[['name', 'hq']].head(10))

# 2. Bar chart (Ratings)
top_ratings = df.sort_values('ratings', ascending=False).head(10)
plt.bar(top_ratings['name'], top_ratings['ratings'])
plt.xticks(rotation=45)
plt.title("Top 10 Companies by Ratings")
plt.show()

# 3. Funnel chart (Reviews)
# 3. Funnel chart (Upside-down triangle style)

top_reviews = df.sort_values('review_count', ascending=False).head(10).dropna()

# Keep DESC order (largest → smallest for upside-down triangle)
top_reviews = top_reviews.sort_values('review_count', ascending=False)

values = top_reviews['review_count'].values
labels = top_reviews['name'].values

max_val = values.max()

# center bars to create triangle shape
left = [(max_val - v) / 2 for v in values]

plt.figure(figsize=(10, 6))

plt.barh(labels, values, left=left, color='skyblue', edgecolor='black')

plt.title("Upside Down Funnel (Top Companies by Reviews)")
plt.xlabel("Review Count")

# biggest at top
plt.gca().invert_yaxis()

# clean funnel look
plt.gca().set_xticks([])
plt.box(False)

plt.tight_layout()
plt.show()
# 4. Line chart (Employees)
top_emp = df.sort_values('employees', ).head(10).dropna()

x = range(len(top_emp))

plt.figure(figsize=(10, 6))

plt.plot(x, top_emp['employees'], marker='o', linestyle='-', color='green')

plt.xticks(x, top_emp['name'], rotation=45, ha='right')

plt.title("Top 10 Companies by Employees")
plt.xlabel("Company")
plt.ylabel("Employee Count")

plt.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()

# 5. Pie chart (Years - Top 5)
top_years = df.sort_values('years', ascending=False).head(5)
plt.pie(top_years['years'], labels=top_years['name'], autopct='%1.1f%%')
plt.title("Top 5 Companies by Years")
plt.show()
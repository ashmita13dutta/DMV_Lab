import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# 1. Load Dataset
# -----------------------------
df = pd.read_csv("dataset_with_deleted_cells.csv")

print("✅ Dataset Loaded\n")

# -----------------------------
# 2. Missing Values Info
# -----------------------------
print("🔍 Missing Values Per Column:\n", df.isnull().sum())
print("\n🔢 Total Missing Values:", df.isnull().sum().sum())

# -----------------------------
# 3. Convert Data Types
# -----------------------------
for col in df.columns:
    try:
        df[col] = pd.to_numeric(df[col])
    except:
        pass

# -----------------------------
# 4. Fill Missing Values
# -----------------------------
num_cols = df.select_dtypes(include=np.number).columns
df[num_cols] = df[num_cols].fillna(df[num_cols].mean())

cat_cols = df.select_dtypes(exclude=np.number).columns
for col in cat_cols:
    if not df[col].mode().empty:
        df[col] = df[col].fillna(df[col].mode()[0])
    else:
        df[col] = df[col].fillna("Unknown")

print("\n✅ Missing Values Filled\n")

# -----------------------------
# 5. Handle Outliers (IQR)
# -----------------------------
for col in num_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    df[col] = np.clip(df[col], lower, upper)

print("✅ Outliers Handled\n")

# -----------------------------
# 6. Save Final Dataset
# -----------------------------
df.to_csv("final_cleaned_dataset.csv", index=False)
print("🎉 Saved as final_cleaned_dataset.csv\n")

# -----------------------------
df_plot = df.head(10)

# -----------------------------
# 1. BAR CHART (Comic Title vs Rating)
# -----------------------------
x_col = "Title"      # change if needed
y_col = "Rating (out of 10)"     # change if needed

plt.figure()
plt.bar(df_plot[x_col].astype(str), df_plot[y_col])

plt.title("Comic Title vs Rating")
plt.xlabel("Comic Title")
plt.ylabel("Rating")
plt.xticks(rotation=45)

plt.show()

# -----------------------------
# 2. PIE CHART (Language Distribution)
# -----------------------------
lang_col = "Language"   # change if needed

value_counts = df_plot[lang_col].value_counts()

plt.figure()
plt.pie(
    value_counts.values,
    labels=value_counts.index.astype(str),
    autopct='%1.1f%%'
)

plt.title("Language Distribution (Top 10 Comics)")
plt.show()

# -----------------------------
# 3. STAIR CHART (Page Count)
# -----------------------------
title_col = "Title"        # change if needed
page_col = "Page Count"    # change if needed

sorted_data = df_plot.sort_values(by=page_col)

plt.figure()
plt.step(range(len(sorted_data)), sorted_data[page_col])

plt.title("Comic Title vs Page Count (Stair Chart)")
plt.xlabel("Index (Sorted Titles)")
plt.ylabel("Page Count")

plt.show()
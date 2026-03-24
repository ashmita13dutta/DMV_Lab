import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('final_cleaned_dataset.csv')

# Replace 'column_name' with your actual column
data = df['Rating (out of 10)']

# Create boxplot
plt.boxplot(data)

plt.xlabel('Values')
plt.ylabel("Rating")
plt.title('Box Plot from CSV Data')

plt.show()
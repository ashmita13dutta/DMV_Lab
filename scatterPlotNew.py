import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv('final_cleaned_dataset.csv')


# data = df[['Page Count', 'Rating (out of 10)']].dropna()
# import pandas as pd


#coorelation

df = pd.read_csv('final_cleaned_dataset.csv')

data = df[['Page Count', 'Rating (out of 10)']].dropna()

corr = data.corr()

print(corr)


#outlier



col = df['Page Count'].dropna()

Q1 = col.quantile(0.25)
Q3 = col.quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = col[(col < lower) | (col > upper)]

print("Outliers:\n", outliers)


#cluster 

import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

df = pd.read_csv('final_cleaned_dataset.csv')

data = df[['Page Count', 'Rating (out of 10)']].dropna()

kmeans = KMeans(n_clusters=3)
data['Cluster'] = kmeans.fit_predict(data)

# Plot clusters
plt.scatter(data['Page Count'], data['Rating (out of 10)'], c=data['Cluster'], cmap='viridis')

plt.xlabel('Page Count')
plt.ylabel('Rating')
plt.title('Clusters in Comic Dataset')

plt.show()

x = data['Page Count']
y = data['Rating (out of 10)']


plt.scatter(x, y, color='blue')
plt.xlabel('Page Count')
plt.ylabel('Rating (out of 10)')
plt.title('Scatter Plot: Page Count vs Rating')

plt.show()
import pandas as pd 
import scipy.stats as stats
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 

df=pd.read_excel('automobile.xlsx')

mean=df['horsepower'].mean()
df['horsepower'].replace(np.nan,mean,inplace=True)

mean=df['price'].mean()
df['price'].replace(np.nan,mean,inplace=True)

pearson_coeff,p_value=stats.pearsonr(df['horsepower'],df['price'])

print(pearson_coeff)
print(p_value)
print()

print(df.corr(method='pearson'))

ax=sns.heatmap(df.corr(method='pearson'))
plt.show()
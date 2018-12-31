import pandas as pd 
import seaborn as sns 
import numpy as np
import matplotlib.pyplot as plt  
from sklearn.linear_model import LinearRegression

df=pd.read_excel('automobile.xlsx')

lm=LinearRegression()

mean=df['highway-mpg'].mean()
df['highway-mpg'].replace(np.nan,mean,inplace=True)

mean=df['horsepower'].mean()
df['horsepower'].replace(np.nan,mean,inplace=True)

mean=df['curb-weight'].mean()
df['curb-weight'].replace(np.nan,mean,inplace=True)

mean=df['engine-size'].mean()
df['engine-size'].replace(np.nan,mean,inplace=True)

mean=df['price'].mean()
df['price'].replace(np.nan,mean,inplace=True)

sns.residplot(df['highway-mpg'],df['price'])
plt.show()

x=df[['horsepower','curb-weight','engine-size','highway-mpg']]
y=df['price']

lm.fit(x,y)

print(lm.intercept_)
print(lm.coef_)

Y=lm.predict(x)

print(Y)

ax1=sns.distplot(df['price'],hist=False,color='r',label='Actual Value')
sns.distplot(Y,hist=False,color='b',label='Fitted Values',ax=ax1)
plt.ylabel("Properties of Car")
plt.show()
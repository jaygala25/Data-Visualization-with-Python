import pandas as pd 
import numpy as np 
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt 
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

df=pd.read_excel('automobile.xlsx')

mean=df['highway-mpg'].mean()
df['highway-mpg'].replace(np.nan,mean,inplace=True)

mean=df['engine-size'].mean()
df['engine-size'].replace(np.nan,mean,inplace=True)

mean=df['curb-weight'].mean()
df['curb-weight'].replace(np.nan,mean,inplace=True)

mean=df['horsepower'].mean()
df['horsepower'].replace(np.nan,mean,inplace=True)

mean=df['price'].mean()
df['price'].replace(np.nan,mean,inplace=True)

'''poly=PolynomialFeatures(degree=3)
print(poly)
print()
poly_x=poly.fit_transform(df[['highway-mpg']])
print(poly_x)
print()

regressor=LinearRegression()
regressor.fit(poly_x,df['price'])
print(regressor)
print()

yhat=regressor.predict(poly.fit_transform([[150]]))
print(yhat)'''

z = df[['highway-mpg']]

Input=[('scale',StandardScaler()),('polynomial',PolynomialFeatures(degree=2)),('model',LinearRegression())]
pipe=Pipeline(Input)
pipe.fit(z,df['price'])

plt.scatter(z,df['price'],color='red')
z=np.linspace(df['highway-mpg'].min(),df['highway-mpg'].max(),100)
y = np.reshape(z, (-1, 1))
ypipe=pipe.predict(y)
print(ypipe)
plt.plot(z,ypipe,color='blue')
plt.xlabel("highway-mpg")
plt.ylabel("Price")
plt.show()
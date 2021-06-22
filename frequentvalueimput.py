import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('C:/users/Naga bharathi/Desktop/datasets/train.csv',usecols=['BsmtQual','FireplaceQu','GarageType','SalePrice'])
print(df.head())
print(df.isnull().sum().sort_values(ascending=True))
print(df.shape)#know how many records in a dataset
df.groupby(['BsmtQual'])['BsmtQual'].count().sort_values(ascending=False).plot.bar() 
plt.show()
df.groupby(['GarageType'])['GarageType'].count().sort_values(ascending=False).plot.bar() 
plt.show()
df.groupby(['FireplaceQu'])['FireplaceQu'].count().sort_values(ascending=False).plot.bar() 
plt.show()
def impute_nan(df,variable):
    most_freq_cat=df[variable].mode()[0]
    df[variable].fillna(most_freq_cat,inplace=True)
for feature in ['BsmtQual','FireplaceQu','GarageType']:
    impute_nan(df,feature)
    print(df.head())

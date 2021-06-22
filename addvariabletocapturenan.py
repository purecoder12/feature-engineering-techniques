import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno
df=pd.read_csv('C:/users/Naga bharathi/Desktop/datasets/train.csv',usecols=['BsmtQual','FireplaceQu','GarageType','SalePrice'])
print(df.head())
print(df.isnull().sum())
df['BsmtQual_var']=np.where(df['BsmtQual'].isnull(),1,0)
print(df.head())
print(df.isnull().sum())



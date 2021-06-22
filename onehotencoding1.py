import pandas as pd
import numpy as np
from pandas.core.reshape.reshape import get_dummies
df=pd.read_csv('C:/Users/Naga bharathi/Desktop/datasets/merctrain.csv',usecols=['X0','X1','X2','X3','X4','X5','X6'])
print(df.head())
for i in df.columns:
    print(df[i].value_counts())
print(df.X1.value_counts().sort_values(ascending=False).head(10))    #Taking out the top 10 frequent category from dataset
lst_10=df.X1.value_counts().sort_values(ascending=False).head(10).index
lst_10=list(lst_10)#converting index into list
print(lst_10)
#now we have to apply one hot encoding for these 10 categories
for categories in lst_10:
    df[categories]=np.where(df['X1']==categories,1,0)
    print(df[categories].head(10))
lst_10.append(df[categories])
print(lst_10)    
   

import numpy as np
import pandas as pd
df=pd.read_csv('C:/users/Naga bharathi/Desktop/datasets/train.csv',usecols=['BsmtQual','FireplaceQu','GarageType','SalePrice'])
def impute_nan(df,variable):
    df[variable+"_new_var"]=np.where(df[variable].isnull(),"unknown",df[variable])
    print(df.head())
    print(df.drop(['BsmtQual','FireplaceQu'],axis=1).head(5))
for features in ['BsmtQual','FireplaceQu']:
        impute_nan(df,features)

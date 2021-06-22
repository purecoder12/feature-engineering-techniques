import pandas as pd
from pandas.core.reshape.reshape import get_dummies
df=pd.read_csv('C:/users/Naga bharathi/Desktop/datascience materials/Feature-Engineering-Live-sessions-master/titanic.csv',usecols=['Embarked'])
print(df.head())
#print(pd.get_dummies(df,drop_first=True).head())
print(df['Embarked'].unique())
df.dropna(inplace=True)
print(pd.get_dummies(df,drop_first=True).head())
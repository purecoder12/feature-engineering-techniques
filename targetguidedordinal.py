import pandas as pd
df=pd.read_csv('C:/Users/Naga bharathi/Desktop/datasets/titanic_train.csv', usecols=['Cabin','Survived'])
df.head()
df['Cabin'].fillna('Missing',inplace=True)
df['Cabin']=df['Cabin'].astype(str).str[0]
print(df.head())
print(df.groupby(['Cabin'])['Survived'].mean().sort_values().index)
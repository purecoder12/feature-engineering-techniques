import pandas as pd
df=pd.read_csv('C:/Users/Naga bharathi/Desktop/datasets/titanic_train.csv', usecols=['Cabin','Survived'])
df.head()
df['Cabin'].fillna('Missing',inplace=True)
df['Cabin']=df['Cabin'].astype(str).str[0]
print(df.head())
mean_ordinal=df.groupby(['Cabin'])['Survived'].mean().to_dict()
print(mean_ordinal)
df['mean_ordinal_encoding']=df['Cabin'].map(mean_ordinal)
print(df.head())
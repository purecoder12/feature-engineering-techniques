import pandas as pd
df=pd.read_csv('C:/Users/Naga bharathi/Desktop/datasets/titanic_train.csv', usecols=['Cabin','Survived'])
df.head()
df['Cabin'].fillna('Missing',inplace=True)
df['Cabin']=df['Cabin'].astype(str).str[0]
print(df.head())
ordinal_labels=df.groupby(['Cabin'])['Survived'].mean().sort_values().index
enumerate(ordinal_labels,0)
ordinal_labels2={k:i for i,k in enumerate(ordinal_labels,0)}
print(ordinal_labels2)
df['Cabin_ordinal_labels']=df['Cabin'].map(ordinal_labels2)#now mapping the cabin with the ordinal_variables2 to feature cabin_ordinal_labels
print(df.head(10))
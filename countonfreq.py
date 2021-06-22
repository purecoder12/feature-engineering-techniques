import pandas as pd
import numpy as np
df=pd.read_csv('C:/Users/Naga bharathi/Desktop/datasets/adult.csv',header=None)
print(df.head())
columns=[1,3,5,6,7,8,9,13]
df=df[columns]
df.columns=['Employment','Degree','Status','Designation','Family_job','Race','Sex','Country']
print(df)
#finding how many categories in each feature
for feature in df.columns[:]:
    print(feature,":",len(df[feature].unique()))
#finding how many numbers in each categories in every feature and map using dictionary
    countryMap=df['Country'].value_counts().to_dict()  
    print(countryMap)
#replacing the categorical variables with the value mapped 
df['Country']=df['Country'].map(countryMap)
print(df.head(20))   



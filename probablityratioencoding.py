#probablity of survived based on the cabin
#probablity of not survived that means died (1-prob(survuved))
#pr(survived)/pr(died)
#dictionary to map cabin with probab_encoded
#replace with categorical feature
import pandas as pd
df=pd.read_csv('C:/Users/Naga bharathi/Desktop/datasets/titanic_train.csv', usecols=['Cabin','Survived'])
#print(df.head())
#replace NAN with other categories or missing
df['Cabin'].fillna('Missing',inplace=True)
print(df.head(10))
print(df['Cabin'].unique())
df['Cabin']=df['Cabin'].astype(str).str[0]#to print the first letter of a category in a given feature
print(df.Cabin.unique())
probabencoding=df.groupby(['Cabin'])['Survived'].mean()
#print(probabencoding)
probabencoding=pd.DataFrame(probabencoding) #creating new data frame as probabencoding
probabencoding['Died']=1-probabencoding['Survived'] #creating a new feature whe it hold the died percentage value
print(probabencoding.head())
#formula : probab survived/probablity of died
#to find probablity value
probabencoding['prob_ratio']=probabencoding['Survived']/probabencoding['Died']
print(probabencoding.head(10))
prob_encoded=probabencoding['prob_ratio'].to_dict()
df['cabin_encoded']=df['Cabin'].map(prob_encoded)
print(df.head(10))
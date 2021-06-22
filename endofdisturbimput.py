import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('C:/users/Naga bharathi/Desktop/datascience materials/Feature-Engineering-Live-sessions-master/titanic.csv',usecols=['Age','Fare','Survived'])
print(df.head())
df.Age.hist(bins=50)
plt.show()
sns.boxplot(x='Age',data=df)
plt.show()
extreme=df.Age.mean()+3*df.Age.std()
def impute_nan(df,variable,median,extreme):
    df[variable+"_end_distribution"]=df[variable].fillna(extreme)
    df[variable].fillna(median,inplace=True)
impute_nan(df,'Age',df.Age.median(),extreme)  
print(df.head())
df.Age.hist(bins=50)
plt.show()
sns.boxplot(x='Age_end_distribution',data=df)
plt.show()
df.Age_end_distribution.hist(bins=10)
plt.show()

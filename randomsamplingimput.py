import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('C:/users/Naga bharathi/Desktop/datascience materials/Feature-Engineering-Live-sessions-master/titanic.csv',usecols=['Age','Fare','Survived'])
#print(df.head())
def random_sampl(df,variable,median):
    df[variable+'_median']=df[variable].fillna(median)
    df[variable+'_random']=df[variable]
    random_sample=df[variable].dropna().sample(df[variable].isnull().sum(),random_state=0)
    random_sample.index=df[df[variable].isnull()].index
    df.loc[df[variable].isnull(),variable+'_random']=random_sample
    print(df.head())
    
median=df.Age.median()    
random_sampl(df,"Age",median)
fig = plt.figure()
ax = fig.add_subplot(111)
df['Age'].plot(kind='kde', ax=ax)
df.Age_median.plot(kind='kde', ax=ax, color='red')
df.Age_random.plot(kind='kde', ax=ax, color='green') 
lines, labels = ax.get_legend_handles_labels()
ax.legend(lines, labels, loc='best')
plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df=pd.read_csv('C:/users/Naga bharathi/Desktop/datascience materials/Feature-Engineering-Live-sessions-master/titanic.csv',usecols=['Age','Fare','Survived'])
df['age_nan']=np.where(df['Age'].isnull(),1,0)
print(df)

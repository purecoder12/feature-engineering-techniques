import pandas as pd
import datetime
today_date=datetime.datetime.today()
print(today_date)
#creating 15 days data
print(today_date-datetime.timedelta(15))
#list comprehension
days=([today_date-datetime.timedelta(x) for x in range(0,15)])
data=pd.DataFrame(days)
data.columns=["date"]
print(data.head())
#retrieving day from a date
data['weekdays']=data['date'].dt.day_name()
print(data)
#create dictionary and map with week days according to rank
dict={'Monday':1,'Tuesday':2,'wednesday':3,'Thursday':4,'Friday':5,'Saturday':6,'Sunday':7}
data['ordinal_mapping']=data['weekdays'].map(dict)
print(data)
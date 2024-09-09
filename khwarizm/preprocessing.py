import pandas as pd 
import numpy as np 

# adding rolling features with defined windows as attributes
# time-series decomposition 
def time_features(dataset:pd.DataFrame) -> pd.DataFrame:
    time_col = ['date','Date','dates','timestamp','TimeStamp','dates']
    for col in time_col: 
        if col in dataset.columns:
            dataset['date'] = pd.to_datetime(dataset[col])
            dataset['Year'] = dataset['date'].dt.year
            dataset['month'] = dataset['date'].dt.month
            dataset['day'] = dataset['date'].dt.day
            dataset['Weekday'] = dataset['date'].dt.weekday
            dataset['Year_week'] = dataset['Year'].astype(str) + '-' + dataset['Weekday'].astype(str)
            dataset['month_day'] = dataset['month'].astype(str) + '-' + dataset['day'].astype(str)
            
    return dataset

        

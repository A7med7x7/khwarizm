import pandas as pd 
import numpy as np

def missing_values(dataframe:pd.DataFrame):    
    desc = pd.DataFrame(index = list(dataset))
    desc['type'] = dataset.dtypes
    desc['count'] = dataset.count()
    desc['nunique'] = dataset.nunique()
    desc['%unique'] = desc['nunique'] /len(dataset) * 100
    desc['null'] = dataset.isnull().sum()
    desc['%null'] = desc['null'] / len(dataset) * 100
    desc = pd.concat([desc,dataset.describe().T.drop('count',axis=1)],axis=1)
    report = desc.sort_values(by=['type','null']).style.background_gradient(axis=0)
    return report
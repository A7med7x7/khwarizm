import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
import seaborn as sns
import pandas as pd
import numpy as np
# adding rolling features with defined windows as attributes
# time-series decomposition 
class Features:

    def __init__(self, dataset:pd.DataFrame,trainset: pd.DataFrame, testset: pd.DataFrame, date_feature: str):
        self.dataset = dataset
        self.trainset = trainset
        self.testset = testset
        self.date_feature = date_feature
        
    @staticmethod
    def rolling(self, feature: str, window: int):
        for dataset in (self.trainset, self.testset):
            dataset[f"{feature}_rolling_max_{window}"] = dataset[feature].rolling(window).max()
            return dataset
    
    @staticmethod
    def time_features(self, dataset: pd.DataFrame) -> pd.DataFrame:
        time_cols = ['date','Date','dates','timestamp','TimeStamp','dates']
        if self.date_feature in time_cols:
            if self.date_feature in dataset.columns:

                dataset['date'] = pd.to_datetime(dataset[col])
                dataset['Year'] = dataset['date'].dt.year
                dataset['month'] = dataset['date'].dt.month
                dataset['day'] = dataset['date'].dt.day
                dataset['Weekday'] = dataset['date'].dt.weekday
                dataset['Year_week'] = dataset['Year'].astype(str) + '-' + dataset['Weekday'].astype(str)
                dataset['month_day'] = dataset['month'].astype(str) + '-' + dataset['day'].astype(str)
                    
        return dataset


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



def plot_numerical_distributions(dataset:pd.DataFrame):
    numerical_cols = dataset.select_dtypes(include=['number']).columns
    n_cols = 3
    n_rows = (len(numerical_cols) + n_cols - 1) // n_cols
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 5 * n_rows))
    axes = axes.flatten()
    for i, col in enumerate(numerical_cols):
        dataset[col] = dataset[col].apply(np.log1p)
        sns.histplot(dataset[col], kde=True, ax=axes[i])
        axes[i].set_title(f'Distribution of {col}')
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])
    plt.tight_layout()
    plt.show()

def plot_target_curve(dataset,time_feature: str,target: str): 
    dataset[target] = np.arange(len(dataset.index))
    plt.rc(
        "axes",
        labelweight="bold",
        labelsize="large",
        titleweight="bold",
        titlesize=16,
        titlepad=10,
    )
    #config InlineBackend.figure_format = 'retina'
    fig, ax = plt.subplots()
    ax.plot(time_feature, target, data=dataset, color='0.75')
    ax = sns.regplot(x=time_feature, y=target, data=dataset, ci=None, scatter_kws=dict(color='0.25'))
    return ax
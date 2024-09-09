import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

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

def plot_target_curve(datase,time_feature: str,target: str): 
    dataset[feature] = np.arange(len(dataset.index))
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
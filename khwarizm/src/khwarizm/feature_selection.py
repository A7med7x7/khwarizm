import contextlib, os,sys
from tqdm import tqdm, trange
@contextlib.contextmanager
def suppress_output():
    with open(os.devnull, 'w') as devnull:
        old_stdout = sys.stdout
        old_stderr = sys.stderr
        sys.stdout = devnull
        sys.stderr = devnull
        try:
            yield
        finally:
            sys.stdout = old_stdout
            sys.stderr = old_stderr

def validate(trainset, testset, target_col, feature_name=None):
    with suppress_output():
        model.fit(trainset.drop(columns=target_col), trainset[target_col])
    pred = model.predict(testset.drop(columns=target_col))
    valid_idx = testset[target_col].notna()
    valid_testset = testset[target_col][valid_idx]
    valid_pred = pred[valid_idx]
    score = mean_squared_error(valid_testset, valid_pred, squared=False)
    if feature_name:
        print(f'Using features: Based_features, {feature_name} | Validation MSE: {score}')
    else:
        print(f'Validation MSE: {score}')
    return score
def feature_combination_analysis(train, target_col, groups, n_splits):
    base_features =  ['LAT', 'LON', 'LST', 'NO2_strat', 'NO2_total', 'NO2_trop', 'TropopausePressure', 'lon_cluster', 'Month', 'Month_Day', 'Year_Week', 'Month_lag1', 'Month_lag2', 'NO2_trop_rolling_max_60', 'NO2_total_rolling_max_60', 'TropopausePressure_rolling_max_60', 'CloudFraction_rolling_max_60', 'Precipitation_rolling_max_60']
    additional_features = [col for col in train.drop(columns=target_col).columns if col not in base_features]

    feature_importances = {}
    for col in additional_features:
        scores = []
        print(f'Evaluating feature: {col}')
        for train_idx, test_idx in cv.split(train[[target_col] + base_features + [col]], train[target_col], groups=groups):
            train_v, test_v = train.iloc[train_idx], train.iloc[test_idx]
            scores.append(validate(train_v[[target_col] + base_features + [col]], test_v[[target_col] + base_features + [col]], target_col, col))
        feature_rmse = np.array(scores).mean()
        feature_importances[col] = feature_rmse
        print(f'Feature {col} with base features, RMSE: {feature_rmse}')
    sorted_features = sorted(feature_importances.items(), key=lambda x: x[1])

    print('Feature importances:')
    for feature, importance in sorted_features:
        print(f'{feature}: {importance}')

    return feature_importances
feature_importances = feature_combination_analysis(train, 'GT_NO2', groups, n_splits)

from statsmodels.stats.outliers_influence import variance_inflation_factor

def removing_high_vif(X):
    
    import pandas as pd

    categorical_features = []
    numerical_features = []

    for i in X.columns:
        if X[i].nunique() < 4:
            categorical_features.append(i)
        else:
            numerical_features.append(i)

    categorical_df = X[categorical_features]
    numerical_df = X[numerical_features]

    vif_data = numerical_df.copy()
    total_columns = len(vif_data.columns)
    columns_to_be_kept = []
    column_index = 0

    for i in range(0, total_columns):
        vif_value = variance_inflation_factor(vif_data, column_index)

        if vif_value <= 6:
            columns_to_be_kept.append(numerical_df.columns[i])
            column_index += 1
        else:
            vif_data = vif_data.drop(columns=[numerical_df.columns[i]])

    return pd.concat([vif_data, categorical_df], axis=1)

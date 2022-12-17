    DEFINE IMPORTANCE OF FEATURES

import pandas as pd
import numpy as np
import time

from sklearn.datasets import make_regression

n_samples = 1000
n_features = 10
n_informative = 3

X, y = make_regression(n_samples=n_samples, n_features=n_features, n_informative=n_informative)

from sklearn.ensemble import RandomForestRegressor
RFR = RandomForestRegressor()
RFR.fit(X, y)

df_feature_importances = pd.DataFrame(RFR.feature_importances_,
                                      columns=["Importance"],
                                      index=col_names)
df_feature_importances = df_feature_importances.sort_values("Importance", ascending=False)
df_feature_importances

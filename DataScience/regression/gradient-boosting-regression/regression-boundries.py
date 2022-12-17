from sklearn.ensemble import GradientBoostingRegressor# Set lower and upper quantile
LOWER_ALPHA = 0.1
UPPER_ALPHA = 0.9# Each model has to be separate


lower_model = GradientBoostingRegressor(loss="quantile",                   
                                        alpha=LOWER_ALPHA)
# The mid model will use the default loss
mid_model = GradientBoostingRegressor(loss="ls")

upper_model = GradientBoostingRegressor(loss="quantile",
                                        alpha=UPPER_ALPHA)

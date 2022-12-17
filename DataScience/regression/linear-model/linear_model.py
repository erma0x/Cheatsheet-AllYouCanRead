#!/usr/bin/python3
#!coding=utf-8

import numpy as np
from sklearn.linear_model import LinearRegression

def LM_stats(x,y): # LINEAR MODEL

    model = LinearRegression()
    x_=np.array(x)
    y_=np.array(y)
    x_=x_.reshape(-1,1)
    y_=y_.reshape(-1,1)

    model.fit(x_, y_)
    model = LinearRegression().fit(x_, y_)
    r_value_ = model.score(x_, y_) # R**2 deve essere maggiore di 0.7
    intercept_=model.intercept_ # non importa
    slope_=model.coef_ # deve essere +
    slope_modified=slope_.tolist()
    slope_modified=slope_modified[0]
    slope_=slope_modified[0]  #np.array([[8]]) to 8
    intercept_modified=intercept_.tolist()
    intercept_=intercept_modified[0]
    item_list=[slope_, intercept_, r_value_]
    return( item_list )

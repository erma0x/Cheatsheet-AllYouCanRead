# Multiple regression PROJECT

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

import sklearn.linear_model import LinearRegression

data = pd.read_csv( path )

x = data[["col1","col2"]] # input 
y = data["col3"]          # target


    # check shapes
print( x.shape,  y.shape) # if are the same we can proceed
if  x.shape !=  y.shape:
    x = x.values.reshape(a,b)
    y = y.values.reshape(c,d)

reg = LinearRegression() # initialize the model
reg.fit(x,y)


    # model performance parameter
R_squared = reg.score(x,y)
coefficents = reg.coef_
intercept = reg.intercept_



    # prediction
x_value = 155.00
reg.predict( x_value )


df = df['X']
predict_data = reg.predict( df )

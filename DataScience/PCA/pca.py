# PCA example 


import numpy as np


# generate random data
a = np.random.normal(size=100)
print(a)

b = np.random.normal(size=100)
print(b)

c = a + b
print(c)


# generate data structure
X = np.c_[a, b, c]
print(X)

from sklearn import decomposition # import decompostiotion of the features with .pca
pca = decomposition.PCA()
pca.fit(X)  

print(pca.explained_variance_)  

#  only the first 2 components are useful
pca.n_components = 2 
X_reduced = pca.fit_transform(X)
X_reduced.shape # final data

print(X_reduced.shape)

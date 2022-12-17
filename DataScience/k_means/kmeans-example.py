from skliearn import preprocessing
from skliearn.cluster impor KMeans
import pandas as pd

number_of_groups = 4 
data = pd.read_csv('filepath.csv')
x = preprocessing.scale(data)
kmeans = KMeans(number_of_groups)
kmeans.fit(x)

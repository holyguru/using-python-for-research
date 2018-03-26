"""
Read in the data as a pandas
 dataframe using pd.read_csv. 
The data can be found at 
https://s3.amazonaws.com/demo-datasets/wine.csv
"""

import pandas as pd
import numpy as np
data = pd.read_csv('https://s3.amazonaws.com/demo-datasets/wine.csv') #read directly from the link






"""
Print the first 5 rows of data using the head() method.
The dataset remains stored as data. Two columns in data are is_red and color,
 which are redundant. Drop color from the dataset, and save the new dataset as numeric_data.
"""
print (data.head(5))

numeric_data=data.drop(['color'],axis=1)
print (numeric_data.head(5))

""""
Scale the data using the sklearn.preprocessing function scale() on numeric_data.
Convert this to a pandas dataframe, and store as numeric_data.
Include the numeric variable names using the parameter columns = numeric_data.columns.
Use the sklearn.decomposition module PCA(), and store this as pca.
Use the fit_transform() function to extract the first two principal components from the data, 
and store this as principal_components.
"""""

import sklearn.preprocessing as skp
scaled_data =skp.scale(numeric_data)
numeric_data =  pd.DataFrame(scaled_data,columns = numeric_data.columns)
#from sklearn.preprocessing import StandardScaler
pca = sklearn.decomposition.PCA(n_components=2)
principal_components = pca.fit(numeric_data).transform(numeric_data)

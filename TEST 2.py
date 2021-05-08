import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage 
import pandas as pd
dataset=pd.read_csv('C:/Users/Amira/Desktop/m1tlc/python/Nouveau dossier/synthetic_control.data',sep='\\t',engine='python')
#dimension des données
print(dataset.shape)
#statistiques descriptives
print(dataset.describe())
##b=np.array(dataset, dtype=float)
##print(b)
from sklearn.preprocessing import normalize
data_scaled= normalize(dataset)
data_scaled=pd.DataFrame(data_scaled, columns=dataset.columns)
data_scaled.head()
X=data_scaled
X.head()

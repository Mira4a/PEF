import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage 
import pandas as pd
dataset=pd.read_csv('C:/Users/Amira/Desktop/m1tlc/python/Nouveau dossier/synthetic_control.data',sep='\\t',engine='python')
#dimension des données
print(dataset.shape)
#statistiques descriptives
print(dataset.describe())
b=np.array(dataset, dtype=float)
print(b)
mat = []        #création d'une liste vide
with open ('C:/Users/Amira/Desktop/m1tlc/python/Nouveau dossier/synthetic_control.data','r') as f :      #ouverture du fichier en mode lecture
    for li in f :       #pour toutes les lignes du fichier :
        s=li.strip('\n\r')      # on enlève les caractère de fin de ligne
        l = s.split(" ")        # on découpe en colonnes
        mat.append(l)           # on ajoute la ligne à la matrice
print(mat)      #affichage de la matrice
import scipy.cluster.hierarchy as sch
dendrogram=sch.dendrogram(sch.linkage(X,method='ward'))

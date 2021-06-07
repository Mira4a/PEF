import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage 
import pandas as pd
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics.cluster import adjusted_rand_score,normalized_mutual_info_score
# dataset=pd.read_csv('synthetic_control.data',sep='\\t',engine='python')
# #dimension des données
# print(dataset.shape)
# #statistiques descriptives
# print(dataset.describe())
# b=np.array(dataset, dtype=float)
# print(b)

mat = []        #création d'une liste vide
with open ('synthetic_control.data','r') as f :      #ouverture du fichier en mode lecture
    for li in f :       #pour toutes les lignes du fichier :
        #print(li)
        s=li.rstrip('\n')    # on enlève les caractère de fin de ligne
        l = s.split()        # on découpe en colonnes
        mat.append(l)           # on ajoute la ligne à la matrice
        #print(l)
#print(mat)      #affichage de la matrice
print(len(mat))

#import scipy.cluster.hierarchy as sch
#dendrogram=sch.dendrogram(sch.linkage(mat,method='ward'))




# setting distance_threshold=0 ensures we compute the full tree.
model = AgglomerativeClustering(distance_threshold=None, n_clusters=6)
model = model.fit(mat)
print(model.labels_)


classe=[]
for i in range(600):
	classe.append(int(i/100))
print(classe)


ARI=adjusted_rand_score(classe, model.labels_)
print(ARI)

NMI=normalized_mutual_info_score(classe, model.labels_)
print(NMI)

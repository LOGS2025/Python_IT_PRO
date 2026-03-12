import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Media por Grupo Salarial
def average(matriz):
    print("Media por Grupo Salarial :",matriz.mean(axis=1))
    print("Media por Año :",matriz.mean(axis=0))
    pass    
'''
- Higher value → **more unstable price growth**
- Lower value → **more stable market**
'''
def volatility(matriz):
    return matriz.std(axis=1)
'''
Long-Term Growth by Income Group
'''
def growth(matriz):
    growth = matriz.iloc[:,-1] - matriz.iloc[:,0]
    print("Growth Matrix: \n\n",growth)
    print("Grupo Salarial con mayor crecimiento de Media del monto/vivienda nueva cada año :",matriz.idxmax())
    print("Grupo Salarial con mayor decrecimiento de Media del monto/vivienda nueva cada año :",matriz.idxmin())

    pass
'''
Mapa de Calor
'''
def heatmap(matriz):
    sns.heatmap(matriz, cmap="coolwarm", center=0)
    plt.show()
    pass

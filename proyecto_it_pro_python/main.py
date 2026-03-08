
'''
1. Recopilar y clasificar los datos de apis o precios 
de materiales, mano de obra, etc.

Guardar porcentajes de costos y variables de precios. Como JSON, CSV y XML

2. Crear un modelo de almacenamiento de datos.

3. Gráficas.
'''

import housing_proccess as hp
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def housing_costs():
    segmento_uma : str
    segmento : str
    superficie : str
    recamara : str
    pcu : str
    tipo_vivienda : str
    modalidad : str
    valor_vivienda : str 
    avance_obra : str
    pass

# El parseo demográfico podemos aproximarlo sabiendo que la población en 
# la Benito Juárez oscila alrededor de 400,000 habitantes. De esto, tenemos 
# que tomar en cuenta el porcentaje de esa población que es Económicamente Activa
# y relacionarlo dentro de las tablas csv's, que ofrecen la cantidad de nuevas viviendas
# construidas por su respectivo rango de edad. Sabiendo esto, podemos unir al 
# modelo de crecimiento por edad, y, así, su demanda a los años aproximados.

# La ecuación
# Pop(time) = pop_actual.edad + time +(-) f_incremento/decremento_pop(edad) 

def demographic_parse():
    rango_edad : str
    rango_salarial : str
    pass

# PARSE DATAFRAMES ON HOUSING COSTS 
def calc_costos_construccion():
    housing_costs()
    pass

# MATH
def costo_final():
    pass

# MATH
def ganancia_total():
    pass

def ofertaDemanda():
    demographic_parse()
    pass

def incertidumbre():
    pass

def main():
    record_financiamiento_csv = []
    records_reg_csv = {}
    # GET the information, only run once
    #hp.get_API_csv()

    # Fill a list of dataframes from each year, obtained from CSV's
    hp.append_csv_financiamiento(record_financiamiento_csv)
    hp.append_csv_registro(records_reg_csv)
    matriz =hp.filter_dataframe(record_financiamiento_csv)
    '''
    Devuelve una matriz con el promedio de cada muestra.
    '''
    #hp.matrix_process(matriz)
    
    # Rellena NaN con 0's 
    matriz.fillna(0)
    
    # Media por Grupo Salarial
    print("Media por Grupo Salarial :",matriz.mean(axis=1))
    print("Media por Año :",matriz.mean(axis=0))
    print("Grupo Salarial con mayor crecimiento de Media del monto/vivienda nueva cada año :",matriz.idxmax())
    print("Grupo Salarial con mayor decrecimiento de Media del monto/vivienda nueva cada año :",matriz.idxmin())

    sns.heatmap(matriz, cmap="coolwarm", center=0)
    plt.show()

    pass


if __name__ == '__main__':
    main()

# Costo(tipo-de-vivienda, tiempo) = f_costo(tipo_de_vivienda,tiempo) + f_costo_demanda(tipo_de_vivienda,tiempo)

# f_costo(tipo_de_vivienda,tiempo) = tipo_de_vivienda(vertical/horizontal,var_precios,m2)

# f_costo_demanda = pop_growth(non-linear,non-exponencial,non-recursive)---f(rango_de_edades)*PEA---cantidad de 
#                       gente @gente que sera parte o es de la PEA
# f_costo_vivienda = P(no_de_casas) + Incremento_m2
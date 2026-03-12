
'''
1. Recopilar y clasificar los datos de apis o precios 
de materiales, mano de obra, etc.

Guardar porcentajes de costos y variables de precios. Como JSON, CSV y XML

2. Crear un modelo de almacenamiento de datos.

3. Gráficas.
'''

'''
- El **Índice SHF de Precios de la Vivienda** mostró en el primer semestre de 2021 una apreciación de 7.1% a nivel nacional en comparación con el mismo periodo de 2020; mientras que en el segundo trimestre de 2021 la apreciación de este fue de 7.8 por ciento.

- El **Índice SHF** **de vivienda nueva** tuvo una variación de 6.5%, mientras que el correspondiente a la **vivienda usada** aumentó 7.6% en el primer semestre de 2021. Durante este periodo se observó una proporción de viviendas usadas igual a 61.5% y 38.5% de viviendas nuevas.

- El precio por metro cuadrado de la **vivienda aumentó 10.9%** en lo que va de 2021 con respecto a 2020, mientras que el de la construcción lo hizo en 6.8 por ciento.
'''



import housing_proccess as hp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pop_model as pm

def housing_costs():
    # segmento_uma : str
    # segmento : str
    # superficie : str
    # recamara : str
    # pcu : str
    # tipo_vivienda : str
    # modalidad : str
    # valor_vivienda : str 
    # avance_obra : str
    pass

    '''
    BJ => Benito Juárez
    m => male
    f => female
    porcentaje de población económicamente activa en la BJ => PPEA
    índice de desarrollo económico => IDE
    PPEA_f_2015 = 0.5225
    PPEA_m_2015 = 0.7366

    PPEA_2020 = 0.74
    IDE_2020 = 0.58
    
    Crecimiento Anual => YrGrowth
    YrGrowth_1990_2020 = 0.0119->0.0117
    '''

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

def oferta():
    demographic_parse()
    pass

def incertidumbre():
    pass

def monteCarlo():
    pass

def main():
    record_financiamiento_csv = []
    records_reg_csv = []
    # GET the information, only run once
    #hp.get_API_csv()

    # Fill a list of dataframes from each year, obtained from CSV's
    hp.append_csv_financiamiento(record_financiamiento_csv)
    records_reg_csv = hp.append_csv_registro(records_reg_csv)
    # Generate a matrix for our financial records
    matriz =hp.filter_dataframe(record_financiamiento_csv)
    '''
    Devuelve una matriz con el promedio de cada muestra.
    '''
    hp.matrix_process(matriz)
    # Rellena NaN con 0's 
    matriz.fillna(0)
    avg_prices = np.array(matriz.mean(axis=0))
    '''
    A simple Monte Carlo simulation does nothing if the only variables are the sample average 
    cost/house and it's std. deviation. And it looks like the following (...). But, if we add other variables
    suited for this project like m^2 price rise, demographic growth distribution, and uncertainty (and knowing
    analytical solutions are impossible),then simulation is the only way to know how the samples will behave in
    X years. And that way, through simulation, distributions are not needed, because the simulation itself will
    show a distribution of random tries.
    '''
    # Media Muestral
    mu = np.mean(avg_prices)
    # Desv Est. Muestral
    sigma = np.std(avg_prices, ddof=1)
#    N = 100_000
#    simulated_prices = np.random.normal(mu,sigma,N)
#    prob = np.mean(simulated_prices > 2)
    reg_df = hp.average_surface_per_housing(records_reg_csv)
    pop_growth_model = pm.linear_regression_for_population()

 

    pass


if __name__ == '__main__':
    main()

# Costo(tipo-de-vivienda, tiempo) = f_costo(tipo_de_vivienda,tiempo) + f_costo_demanda(tipo_de_vivienda,tiempo)

# f_costo(tipo_de_vivienda,tiempo) = tipo_de_vivienda(vertical/horizontal,var_precios,m2)

# f_costo_demanda = pop_growth(non-linear,non-exponencial,non-recursive)---f(rango_de_edades)*PEA---cantidad de 
#                       gente @gente que sera parte o es de la PEA
# f_costo_vivienda = P(no_de_casas) + Incremento_m2

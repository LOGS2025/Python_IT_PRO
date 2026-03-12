
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
from sklearn.linear_model import LinearRegression 


# Returns the average of all average prices for a house
def housing_costs(avg_prices):
    # Media Muestral
    mu = np.mean(avg_prices)
    return mu

def ppea_population(population_some_year : float):
    rango_edad : str
    rango_salarial : str
    ppea : int
    pass

# A través de la regresión linear propuesta para determinar el crecimiento poblacional, obtenemos
# la población en el año pasado como argumento.
def demographic_parse(growth_model : sklearn.LinearRegression,year : float)->float:
    population_that_year = 0
    ##############################
    population_that_year = growth_model.intercept_ + growth_model.coef_ * year
    return population_that_year

# PARSE DATAFRAMES ON HOUSING COSTS 
def calc_costos_construccion(avg_prices):
    avg_avg_house_price = housing_costs(avg_prices)
    pass

# MATH
def costo_final():
    pass


def oferta(record_csv,population_per_year):


    pass

def incertidumbre():
    pass

def monteCarlo():
    pass

def main():
    #year_complete = [1980,1990,2000,2005,2010,2015,2020]
    year = [2000,2005,2010,2015,2020]
    #pop_complete = [480_741.00,407_811.00,360_478.00,355_017.00,385_439.00,417_416.00,432_259.00]
    pop = [360_478.00,355_017.00,385_439.00,417_416.00,432_259.00]
    record_financiamiento_csv = []
    pop_growth_model = pm.linear_regression_for_population(year,pop) 

    # GET the information, only run once
    #hp.get_API_csv()

    # Fill a list of dataframes from each year, obtained from CSV's
    hp.append_csv_financiamiento(record_financiamiento_csv)

    filter = hp.filter_dataframe(record_financiamiento_csv)
    matriz = hp.get_matrix(filter)  # Generate a matrix for our financial records
    hp.matrix_process(matriz)       #Devuelve una matriz con el promedio de cada muestra.
    matriz.fillna(0)                # Rellena NaN con 0's 
    avg_prices = np.array(matriz.mean(axis=0))

    # Media Muestral
    mu = np.mean(avg_prices)
    # Desv Est. Muestral
    sigma = np.std(avg_prices, ddof=1)
#   N = 100_000
#   simulated_prices = np.random.normal(mu,sigma,N)
#   prob = np.mean(simulated_prices > 2)

    table_financiamiento = hp.total_instances_of_housing(filter)
    table_financiamiento.fillna(0)
    sum = table_financiamiento.sum(1) # Devuelve las instancias de vivienda nuevas totales por año
    print(sum)
    pass


if __name__ == '__main__':
    main()

'''
A simple Monte Carlo simulation does nothing if the only variables are the sample average 
cost/house and it's std. deviation. And it looks like the following (...). But, if we add other variables
suited for this project like m^2 price rise, demographic growth distribution, and uncertainty (and knowing
analytical solutions are impossible),then simulation is the only way to know how the samples will behave in
X years. And that way, through simulation, distributions are not needed, because the simulation itself will
show a distribution of random tries.
'''

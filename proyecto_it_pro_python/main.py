
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



from pandas.io.pytables import performance_doc
from data_functions import volatility
import housing_proccess as hp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pop_model as pm
from sklearn.linear_model import LinearRegression 


# A través de la regresión linear propuesta para determinar el crecimiento poblacional, obtenemos
# la población en el año pasado como argumento.
def demographic_parse(growth_model : sklearn.LinearRegression,year : float)->float:
    population_that_year = 0
    ##############################
    population_that_year = growth_model.intercept_ + growth_model.coef_ * year
    return population_that_year

def monteCarlo(price_question : float, years : int):
    P0 = 0.758   # current average price (millions)
    # Data from 2020-2021
    mu = 0.109   # growth
    sigma = 0.73 # volatility

    sims = 10000

    paths = np.zeros((years, sims))
    paths[0] = P0

    for t in range(1, years):
        Z = np.random.normal(0,1,sims)
        paths[t] = paths[t-1] * np.exp((mu - 0.5*sigma**2) + sigma*Z)

    plt.plot(paths[:, :100])
    #plt.xlabel("Years")
    #plt.ylabel("Average house price (millions)")
    #plt.show()

    future_prices = paths[-1]
    prob = np.mean(future_prices > price_question)
    print(f"Probabilidad de que el costo promedio de una casa en {years} años sea de {price_question} millones de pesos es :",prob)
    pass

def main():
    #year_complete = [1980,1990,2000,2005,2010,2015,2020]
    year = [2000,2005,2010,2015,2020]
    #pop_complete = [480_741.00,407_811.00,360_478.00,355_017.00,385_439.00,417_416.00,432_259.00]
    pop = [360_478.00,355_017.00,385_439.00,417_416.00,432_259.00]
    record_financiamiento_csv = []
    pop_growth_model = pm.linear_regression_for_population(year,pop) 
    growth = 0.109

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

    table_financiamiento = hp.total_instances_of_housing(filter)
    table_financiamiento.fillna(0)
    houses_per_year = table_financiamiento.sum(1) # Devuelve las instancias de vivienda nuevas totales por año
    print(type(houses_per_year))
    print("Mu Casas Por Año desde 2000 hasta 2020",np.mean(houses_per_year))
    print("Std Casas Por Año desde 2000 hasta 2020",np.std(houses_per_year))
    print("Mu Promedio de los promedios de costo por casa desde 2000 hasta 2020",mu)
    print("Std de costo por casa desde 2000 hasta 2020",sigma)
    print("Aumento anual de 2020 a 2021 del precio del m2",growth)
    print("Modelo de regresión lineal con r2=91% de 2000-2020 (coef,intercept):",pop_growth_model.coef_,pop_growth_model.intercept_)
    #print("Volatilidad ",volatility(matriz))
    monteCarlo(2.3,5) # Probability of a house costing 2.3 million in 5 years
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

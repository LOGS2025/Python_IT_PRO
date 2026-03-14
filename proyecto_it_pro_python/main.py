'''
- El **Índice SHF de Precios de la Vivienda** mostró en el primer semestre de 2021 una apreciación de 7.1% a nivel nacional en comparación con el mismo periodo de 2020; mientras que en el segundo trimestre de 2021 la apreciación de este fue de 7.8 por ciento.

- El **Índice SHF** **de vivienda nueva** tuvo una variación de 6.5%, mientras que el correspondiente a la **vivienda usada** aumentó 7.6% en el primer semestre de 2021. Durante este periodo se observó una proporción de viviendas usadas igual a 61.5% y 38.5% de viviendas nuevas.

- El precio por metro cuadrado de la **vivienda aumentó 10.9%** en lo que va de 2021 con respecto a 2020, mientras que el de la construcción lo hizo en 6.8 por ciento.
'''

growth_housing_prices = ( 0.071 + 0.078 ) / 2
growth_m2 = 0.109
growth_construction = 0.068

from pandas.io.pytables import performance_doc
from data_functions import volatility
import housing_proccess as hp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pop_model as pm
from sklearn.linear_model import LinearRegression 
import seaborn as sns

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
    years = [2000,2005,2010,2015,2020]
    pop = [360_478.00,355_017.00,385_439.00,417_416.00,432_259.00]
    record_financiamiento_csv = []
    pop_growth_model = pm.linear_regression_for_population(years,pop) 

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
    mean_houses_per_year= table_financiamiento.mean(1)
    pred_casas = sr_tm_yr(houses_per_year,2030,0.99) # Con w=0.99
    avg_prices_series = pd.Series(avg_prices,range(2000,2026))
    pred_precios = []
    pred_precios.append(sr_tm_yr(avg_prices_series,2040,0.3)) # Con w=0.99
    pred_precios.append(sr_tm_yr(avg_prices_series,2040,0.5)) # Con w=0.99
    pred_precios.append(sr_tm_yr(avg_prices_series,2040,0.7)) # Con w=0.99
    pred_precios.append(sr_tm_yr(avg_prices_series,2040,0.9)) # Con w=0.99
    pred_pop = sr_tm_yr_population(pop_growth_model,2026)
    sr_holt_linear_yr(avg_prices_series,2025,0.501,0.072)

    mu_casas_t = mean_houses_per_year.sum()/len(mean_houses_per_year.values)
    print("\n\n\t\t Promedio desde 1980 hasta 2025 de casas construidas\n\n",mu_casas_t) # 596.88
    #   El **Índice SHF** **de vivienda nueva** tuvo una variación de 6.5%
    variation_new_housing = 0.065
    #   Así que ahora tenemos el la distribución de Poisson de casas
    houses_t = np.random.poisson(mu_casas_t)


    corr_ = {
        "cost_per_year" : avg_prices,
        "house_per_year" : houses_per_year,
        "pop_per_year" : pred_pop
    }

    print("\n\n\t\tCorrelation between data from 2000-2025\n\n")
    _corr_df = pd.DataFrame(corr_)
    corr_methods(_corr_df)

    print("\n\n\t\tCorrelation between data from 2010-2025\n\n")
    _corr_df_2010_2025 = _corr_df.loc[2010:2025]
    corr_methods(_corr_df_2010_2025)

    #plt.plot(mean_houses_per_year.index, mean_houses_per_year.values, label="Promedio de casas por año")
    #plt.plot(houses_per_year.index, houses_per_year.values, label="Total de casas por año")
    plt.plot(mean_houses_per_year.index, avg_prices_series.values, label="Precios promedio por año")
    plt.plot(range(2000,2040), pred_precios[0], label="Series tiempo w = 0.3")
    plt.plot(range(2000,2040), pred_precios[1], label="Series tiempo w = 0.5")
    plt.plot(range(2000,2040), pred_precios[2], label="Series tiempo w = 0.7")
    plt.plot(range(2000,2040), pred_precios[3], label="Series tiempo w = 0.9")
    plt.legend()
    #plt.show()

    #print(type(houses_per_year))
    #print("Mu Casas Por Año desde 2000 hasta 2020",np.mean(houses_per_year))
    #print("Std Casas Por Año desde 2000 hasta 2020",np.std(houses_per_year))
    #print("Mu Promedio de los promedios de costo por casa desde 2000 hasta 2020",mu)
    #print("Std de costo por casa desde 2000 hasta 2020",sigma)
    #print("Aumento anual de 2020 a 2021 del precio del m2",growth)
    #print("Modelo de regresión lineal con r2=91% de 2000-2020 (coef,intercept):",pop_growth_model.coef_,pop_growth_model.intercept_)
    #print("Volatilidad ",volatility(matriz))
    pass


def sr_tm_yr(series_with_data, end_year:int, w_value:float)->list:
    '''
    SERIES DE TIEMPO
    PME_t = PME_t_1 + w(Y_t - PME_t_1)
    Donde PME es el promedio móvil
    y Y_t es la observación original
    '''
    PME_t_1 = series_with_data.get(2000)

    casas_w_1 = []
    duration = range(2000,end_year)

    PME_t__1 = 0
    for year in duration:
        # Obtain new mean
        Y_t = series_with_data.get(year,PME_t__1)

        PME_t = PME_t_1 + w_value*(Y_t - PME_t_1)

        PME_t__1 = PME_t_1
        PME_t_1 = (PME_t+PME_t_1)/2

        casas_w_1.append(PME_t)
    return casas_w_1

def sr_holt_linear_yr(series_with_data, end_year:int,alpha:float,beta:float):
    '''
    HOLT LINEAR
    '''
    I_t_1 = series_with_data.get(2000)
    L_t = I_t_1
    b_t = series_with_data.get(2001) - series_with_data.get(2000) 
    forecast = []
    duration = range(2000,end_year)
    f_t = L_t + 1*b_t
    forecast.append(f_t)

    L_t_1 = L_t
    b_t_1 = b_t

    for year in duration:

        I_t = series_with_data.get(year)
        L_t = alpha*I_t + ( 1-alpha )*( L_t_1 + b_t_1 )
        b_t = beta*( L_t - L_t_1 ) + (1-beta)*b_t_1

        f_t = L_t_1 + 1*b_t_1
        print(f_t)
        forecast.append(f_t)

        L_t_1 = L_t
        b_t_1 = b_t
    
    pass


def sr_tm_yr_population(pop_growth_model, year):
    population_ = []
    for year in range(2000,year):
        population_.append(demographic_parse(pop_growth_model,year))
    return population_

def corr_methods(_corr_df):
    pearson_corr = _corr_df.corr(method='pearson')  
    print(pearson_corr)

    spearman_corr = _corr_df.corr(method='spearman')
    print(spearman_corr)

    kendall_corr = _corr_df.corr(method='kendall')
    print(kendall_corr)

    corr_value = _corr_df['cost_per_year'].corr(_corr_df['house_per_year'])
    print("Correlation between cost and instances of new housing:", corr_value)

    corr_value = _corr_df['pop_per_year'].corr(_corr_df['house_per_year'])
    print("Correlation between population and instances of new housing:", corr_value)

    corr_value = _corr_df['pop_per_year'].corr(_corr_df['cost_per_year'])
    print("Correlation between population and cost of new housing:", corr_value)
    pass

# A través de la regresión linear propuesta para determinar el crecimiento poblacional, obtenemos
# la población en el año pasado como argumento.
def demographic_parse(growth_model : sklearn.LinearRegression,year : float)->float:
    return growth_model.predict([[year]])[0]




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

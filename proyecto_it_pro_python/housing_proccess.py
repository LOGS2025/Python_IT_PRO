import pandas as pd
import gobCSV_housing as housing
import matplotlib.pyplot as plt
import numpy as np


def get_API_csv():
    dimensiones_financiamiento = 'organismo,grupo_organismo,rango_salarial,valor_vivienda,tipo_credito,modalidad'
    dimensiones_conavi = 'rango_edad,rango_salarial,tipo_vivienda,valor_vivienda,modalidad'
    dimensiones_FOVISSSTE = 'rango_edad,rango_salarial,valor_vivienda,modalidad'
    dimensiones_infonavit = 'rango_edad,rango_salarial,valor_vivienda,vivienda,modalidad'
    dimensiones_CNBV = 'rango_edad,rango_salarial,valor_vivienda,modalidad'
    dimensiones_inv_vivienda = 'avance_obra,segmento_uma,tipo_vivienda,pcu,segmento'
    dimensiones_reg_vivienda = 'segmento,segmento_uma,tipo_vivienda,superficie,recamara'
    dimensiones_verificacion = 'segmento,segmento_uma,tipo_vivienda,superficie,recamara'
    dimensiones_produccion = 'segmento,segmento_uma,tipo_vivienda,superficie,recamara'
    for año in range(26):
        # Run once
        housing.API_gob_vivienda_builder("GetFinanciamiento",dimensiones_financiamiento,(año+2000))
        housing.API_gob_vivienda_builder("GetRegistro",dimensiones_reg_vivienda,(año+2000))

def append_csv_financiamiento(lista_csv : list) -> list:
    def to_millions(lista_csv : list) -> list: 
        # Transform to millions
        for i, dataframe in enumerate(lista_csv):
            dataframe["monto en millones"] = dataframe["monto"] / 1_000_000
            lista_csv[i] = dataframe[dataframe["modalidad"] == "Viviendas nuevas"]
        return lista_csv
    for año in range(26):
        try:
            # Dinero en casas nuevas, rango salarial
            df_tmp = pd.read_csv(f"./csv/GetFinanciamiento.{año+2000}.csv")
            df_tmp["year"]=(año+2000)
            lista_csv.append(df_tmp)
        except FileNotFoundError:
            print("No existe registro")
            continue
    to_millions(lista_csv)
    return lista_csv

def append_csv_registro(dict_csv : dict) -> dict:
    for año in range(26):
        try:
            # Casas nuevas, recámara, superficie y si es vertical u horizontal
            dict_csv[año+2000]=(pd.read_csv(f"./csv/GetRegistro.{año+2000}.csv"))
        except FileNotFoundError:
            print("No existe registro")
            continue
    return dict_csv

'''
Varianza entre Viviendas Nuevas por rango salarial -- DEMANDA DE CASAS POR AÑO
Correlación entre la población y las Viviendas Nuevas

Correlación entre el aumento o no de precio y la población
Correlación entre costo de vivienda con precio del m2

salario_mínimo xbarra xondulada xmo
salario xbarra xondulada xmo
'''

def medidas_tendencia_central(lista_csv : list) -> pd.DataFrame:

    def export_results(lista_csv : list)->None:
        lista_csv.to_csv("FinalRes.csv",index=False)
        final_csv = pd.merge(lista_csv, lista_csv, on="rango_salarial", how="outer")
        final_csv.to_csv("Final.csv",index=False)
        pass

    filter = []
    for dataframe in lista_csv:
        year = dataframe["year"].iloc[0]

        df_whole = dataframe.groupby("rango_salarial").agg(
            sum=("monto en millones", "sum"),
            mean=("monto en millones", "mean"),
            min=("monto en millones", "min"),
            max=("monto en millones", "max"),
            instancias=("acciones", "sum")
        )
        # Add year column
        df_whole["year"] = year
        df_whole = df_whole.reset_index()
        df_whole["mean cost per house"] = df_whole["sum"]/df_whole["instancias"]

        filter.append(df_whole)
    concat_df = pd.concat(filter, ignore_index=True)
    '''
    rango_salarial          sum        mean       min         max  instancias  year  mean cost per house
    0    2.6 o menos   842.724567  105.340571  0.651417  461.095188         252  2025             3.344145
    1    2.61 a 4.00   205.720149   29.388593  0.500000   86.657585          79  2025             2.604053
    2    4.01 a 6.00   413.665563   51.708195  0.980727  212.163304         191  2025             2.165788
    3    6.01 a 9.00   682.033467   85.254183  1.124899  378.473097         270  2025             2.526050
    4   9.01 a 12.00   601.645656  100.274276  6.528995  253.313862         221  2025             2.722379
    5      Más de 12  1455.127504  207.875358  0.894751  972.203085         356  2025             4.087437
    '''
    central_tendency_df_dict = {"avg_cost/house": {}}
    for dataframe in filter:
        for i in range(26):
            try:
                year = dataframe.loc[i, "year"]
                salario = dataframe.loc[i,"rango_salarial"]
                value = dataframe.loc[i, "mean cost per house"]
                # Make a dict with the mean cost per house, per year per salario
                central_tendency_df_dict["avg_cost/house"][salario,year] = value
            except KeyError:
                continue

    central_tendency_df = pd.DataFrame(central_tendency_df_dict)
    central_tendency_df.index = pd.MultiIndex.from_tuples(
        central_tendency_df.index,
        names=["rango_salarial", "year"]
    )
    central_tendency_df.to_csv("Central_tendency.csv",index=True)
    central_tendency_df = pd.read_csv("./Central_tendency.csv")

    # Ahora procesamos las medias de las "¿muestras?" y encontramos la media muestral, varianza, mediana, moda:
    matrix = central_tendency_df.pivot(
        index="rango_salarial",
        columns="year",
        values="avg_cost/house"
    )
    matrix_clean = matrix.rename_axis(columns=None).reset_index()
    print(matrix_clean)
    print(matrix.pct_change(axis=1))
    #print(matrix)
    #export_results(results)
    #print(matrix.T.plot())
    
    return concat_df

def medidas_generales(lista_csv : list) -> pd.DataFrame:

    def export_results()->None:
        results.to_csv("FinalRes.csv",index=False)
        final_csv = pd.merge(results, lista_csv, on="rango_salarial", how="outer")
        final_csv.to_csv("Final.csv",index=False)
        pass

    results = []
    for dataframe in lista_csv:
        year = dataframe["year"].iloc[0]

        df_whole = dataframe.groupby("rango_salarial").agg(
            count=("monto en millones", "count"),
            sum=("monto en millones", "sum"),
            mean=("monto en millones", "mean"),
            min=("monto en millones", "min"),
            max=("monto en millones", "max"),
            instancias=("acciones", "sum")
        )

        df_whole["year"] = year
        df_whole = df_whole.reset_index()

        results.append(df_whole)
    concat_df = pd.concat(results, ignore_index=True)

    export_results
    
    return concat_df

# Promedio del monto total por rango salarial
def media_rangos_salarial_plot(results : list ,lista_csv : list)->None:

    def get_labels()->set:
        labels : set
        for dataframe in lista_csv:
            labels=(dataframe["rango_salarial"].unique())
        return labels
    
    for label in get_labels:
        filtro=results[results["rango_salarial"]==label]
        plt.plot(filtro["year"],filtro["mean"],label=label)

    plt.title("Media por Rango salarial")
    plt.legend()
    plt.show()

# Número de viviendas nuevas por rango salarial
def instancias_rangos_salarial_plot(results : list ,lista_csv : list)->None:

    def get_labels()->set:
        labels : set
        for dataframe in lista_csv:
            labels=(dataframe["rango_salarial"].unique())
        return labels
    
    for label in get_labels:
        filtro=results[results["rango_salarial"]==label]
        plt.plot(filtro["year"],filtro["instancias"],label=label)

    plt.title()
    plt.legend()
    plt.show()

'''
Sabiendo la tendencia actual del monto total por viviendas nuevas y la construcción de estas, ahora
encontraremos al porcentaje anual de Viviendas nuevas que son verticales u horizontales.

De acuerdo a la API:

La API de Registro de Vivienda proporciona información sobre proyectos de oferta habitacional, 
tanto de 

                    vivienda nueva como usada, 

registrados en conjuntos habitacionales o en el mercado abierto individual.

Estos productos son susceptibles de recibir financiamiento por parte de los 
Organismos Nacionales de Vivienda (ONAVIS), la banca comercial o intermediarios financieros como las Sofoles y Sofomes.
'''

def instancias_superficie(records_reg_csv : dict)->None:
    results = []
    for year in (range(2000,2026)): # records_reg_csv holds dicts
        try:
            reg_df =records_reg_csv[year]
        except KeyError:
            continue
        reg_df["year"]=year
        results.append(reg_df)
    pass

# Árbol de decisiones

# Matriz de confusión

# Curvas ROC


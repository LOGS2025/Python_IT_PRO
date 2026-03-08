import pandas as pd
import gobCSV_housing as housing
import matplotlib.pyplot as plt
import numpy as np

dimensiones_financiamiento = 'organismo,grupo_organismo,rango_salarial,valor_vivienda,tipo_credito,modalidad'
dimensiones_reg_vivienda = 'segmento,segmento_uma,tipo_vivienda,superficie,recamara'


record_financiamiento_csv = []
record_registro_csv = []
records_reg_csv = {}
results = []

for año in range(26):
    # Run once
    #df_export = housing.API_gob_vivienda_builder("GetFinanciamiento",dimensiones_financiamiento,(año+2000))
    #df_export = housing.API_gob_vivienda_builder("GetRegistro",dimensiones_reg_vivienda,(año+2000))
    try:
        # Dinero en casas nuevas, rango salarial
        df_tmp = pd.read_csv(f"./csv/GetFinanciamiento.{año+2000}.csv")
        df_tmp["year"]=(año+2000)
        record_financiamiento_csv.append(df_tmp)
        # Casas nuevas, recámara, superficie y si es vertical u horizontal
        records_reg_csv[año+2000]=(pd.read_csv(f"./csv/GetRegistro.{año+2000}.csv"))
    except FileNotFoundError:
        print("No existe registro")
        continue

# Transform to millions
for i, dataframe in enumerate(record_financiamiento_csv):
    dataframe["monto en millones"] = dataframe["monto"] / 1_000_000
    record_financiamiento_csv[i] = dataframe[dataframe["modalidad"] == "Viviendas nuevas"]

for dataframe in record_financiamiento_csv:

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

labels : set
labels=(dataframe["rango_salarial"].unique())

final_results = pd.concat(results, ignore_index=True)
#final_results.to_csv("FinalRes.csv",index=False)
#final_csv = pd.merge(final_results, dataframe, on="rango_salarial", how="outer")
#final_csv.to_csv("Final.csv",index=False)

# First group by rango_salarial

# Promedio del monto total por rango salarial
for label in labels:
    filtro=final_results[final_results["rango_salarial"]==label]
    plt.plot(filtro["year"],filtro["mean"],label=label)
plt.legend()
plt.show()

# Número de viviendas nuevas por rango salarial
for label in labels:
    filtro=final_results[final_results["rango_salarial"]==label]
    plt.plot(filtro["year"],filtro["instancias"],label=label)
plt.legend()
plt.show()

# Árbol de decisiones

# Matriz de confusión

# Curvas ROC


'''
Varianza entre Viviendas Nuevas por rango salarial -- DEMANDA DE CASAS POR AÑO
Correlación entre la población y las Viviendas Nuevas

Correlación entre el aumento o no de precio y la población
Correlación entre costo de vivienda con precio del m2

salario_mínimo xbarra xondulada xmo
salario xbarra xondulada xmo
'''

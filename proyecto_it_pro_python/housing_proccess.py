import pandas as pd
import gobCSV_housing as housing

dimensiones_financiamiento = 'organismo,grupo_organismo,rango_salarial,valor_vivienda,tipo_credito,modalidad'

list_csv = []
for año in range(26):
    df_export = housing.API_gob_vivienda_builder("GetFinanciamiento",dimensiones_financiamiento,(año+2000))
    list_csv.append(pd.read_csv(f"./csv/GetFinanciamiento.{año+2000}.csv"))



# Transform to millions
for dataframe in list_csv:
    # Add a column and make numbers into millions
    dataframe["monto en millones"] = dataframe["monto"] / 1000000
    # Select only Viviendas nuevas inside our dataframe
    dataframe = dataframe[dataframe["modalidad"]=="Viviendas nuevas"]

# Print information
for dataframe in list_csv:    
    df_whole = dataframe.groupby("rango_salarial")["monto en millones"].agg(["count","sum","mean","min","max"])
    df_whole["instancias"] = dataframe.groupby("rango_salarial")["acciones"].agg(["sum"])
    print(df_whole)


import pandas as pd
import gobCSV_housing as housing

dimensiones_financiamiento = 'organismo,grupo_organismo,rango_salarial,valor_vivienda,tipo_credito,modalidad'
dimensiones_reg_vivienda = 'segmento,segmento_uma,tipo_vivienda,superficie,recamara'

record_financiamiento_csv = []
record_registro_csv = []
records_reg_csv = {}
for año in range(26):
    # Run once
    #df_export = housing.API_gob_vivienda_builder("GetFinanciamiento",dimensiones_financiamiento,(año+2000))
    #df_export = housing.API_gob_vivienda_builder("GetRegistro",dimensiones_reg_vivienda,(año+2000))
    try:
        # Dinero en casas nuevas, rango salarial
        record_financiamiento_csv.append(pd.read_csv(f"./csv/GetFinanciamiento.{año+2000}.csv"))
        # Casas nuevas, recámara, superficie y si es vertical u horizontal
        record_registro_csv.append(pd.read_csv(f"./csv/GetRegistro.{año+2000}.csv"))
    except FileNotFoundError:
        print("No existe registro")
        continue

# Transform to millions
for dataframe in record_financiamiento_csv:
    # Add a column and make numbers into millions
    dataframe["monto en millones"] = dataframe["monto"] / 1000000
    # Select only Viviendas nuevas inside our dataframe
    dataframe = dataframe[dataframe["modalidad"]=="Viviendas nuevas"]


# Print information
for dataframe in record_financiamiento_csv:    
    df_whole = dataframe.groupby("rango_salarial")["monto en millones"].agg(["count","sum","mean","min","max"])
    df_whole["instancias"] = dataframe.groupby("rango_salarial")["acciones"].agg(["sum"])
    print(df_whole)

'''
Varianza entre Viviendas Nuevas por rango salarial 
Correlación entre la población y las Viviendas Nuevas
Varianza del precio
Correlación entre el aumento o no de precio y la población
Correlación entre costo de vivienda con precio del m2
'''

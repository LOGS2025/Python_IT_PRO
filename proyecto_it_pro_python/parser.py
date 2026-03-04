import pandas as pd

df_Financiamiento = pd.read_csv("./csv/GetFinanciamiento.csv")
df_FOVISSSTE = pd.read_csv("./csv/GetFOVISSSTE.csv")
df_CNBV = pd.read_csv("./csv/GetCNBV.csv")
df_Registro = pd.read_csv("./csv/GetRegistro.csv")

data = [df_Financiamiento,df_FOVISSSTE,df_CNBV,df_Registro]

# JOIN DATAFRAMES TOGETHER
'''
For this part, it is necessary to determine if multiple institutions 
have recorded the same buildings or operations. In which case, 
dataframes may not be joined together. The difference between them 
can be found when counting the new housing built recorded by each of them.
'''

df_concat = pd.concat([df_CNBV,df_Financiamiento,df_FOVISSSTE],ignore_index=True)

df_concat.to_csv("Concat.csv",index=False)

# for db in data:
#     if "modalidad" in db.columns:
#         print(f"From")
#         print((db["modalidad"] == 'Viviendas nuevas').value_counts())
#         print("-----------------------")
#     else:
#         print("modalidad no disponible")
# print("##################################")
# print(df_Financiamiento.describe())
# print("##################################")
# df_monto_modalidad = df_Financiamiento[["monto","modalidad"]]






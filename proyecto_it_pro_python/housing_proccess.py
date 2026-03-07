import pandas as pd

list_csv = []

df = (pd.read_csv("./csv/GetCNBV.csv"))
list_csv.append((pd.read_csv("./csv/GetFinanciamiento.csv")))
df2 = (pd.read_csv("./csv/GetFOVISSSTE.csv"))
df3 = (pd.read_csv("./csv/GetRegistro.csv"))

group = df.groupby("modalidad")["monto"].agg(["count","sum","mean"])

print(group)
for dataframe in list_csv:
    print(type(dataframe))
    print(dataframe.groupby("modalidad")["monto"].agg(["count","sum","mean"]))

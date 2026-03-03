import pandas
import requests


años = '2025'
clave_estado = '09'
clave_municipio = '014'
dimensiones = 'destino_credito,grupo_organismo,genero,organismo,zona,modalidad,rango_salarial,valor_vivienda,tipo_credito'

params=f"GetFinanciamiento/{años}/{clave_estado}/{clave_municipio}/{dimensiones}"

url=f"https://sniiv.sedatu.gob.mx/api/CuboAPI/{params}"
#https://sniiv.sedatu.gob.mx/api/CuboAPI/GetFinanciamiento/2024,2025/00/000/destino_credito,grupo_organismo,genero,organismo

print(url)

r = requests.get(url)

print(r.status_code)

datos = r.json()

df = pandas.DataFrame(datos)
df.to_csv("conavi.csv",index=False)


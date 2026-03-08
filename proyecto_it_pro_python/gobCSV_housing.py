'''
Source : https://sniiv.sedatu.gob.mx/Reporte/Datos_abiertos
Obtenidos el 2026-03-02

Se analizará por medio de las apis proporcionadas únicamente.
'''

import pandas
import requests

############## FACTORY FOR API CLASS ################

class API_gob_vivienda_builder():
    años : int
    clave_estado = '09'
    clave_municipio = '014'
    url : str
    df : pandas.DataFrame

    def __init__(self, Get_Function : str, dimensiones : str, año : int):
        self.dimensiones = dimensiones
        self.años = año
        params=f"{Get_Function}/{self.años}/{self.clave_estado}/{self.clave_municipio}/{dimensiones}"
        self.url=f"https://sniiv.sedatu.gob.mx/api/CuboAPI/{params}"
       
        r = requests.get(self.url)
        print(r.status_code)
        
        self.df = self.gen_df(r)
        if self.df.empty:
           print(f"Dataframe {Get_Function} is empty\n\tExiting...")
           return
        else:
            self.export_to_csv(Get_Function)
        pass

    def export_to_csv(self, nombre_CSV : str):
        self.df.to_csv(f"./csv/{nombre_CSV}.{self.años}.csv", index=False)
        print("Exported to CSV")
        pass

    def __repr__(self) -> str:
        return self.url 

    def gen_df(self, r : requests.models.Response) -> pandas.DataFrame:
        return pandas.DataFrame(r.json())

############# END OF FACTORY FUNCTION #############


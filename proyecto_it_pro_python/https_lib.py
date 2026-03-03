'''
Source : https://sniiv.sedatu.gob.mx/Reporte/Datos_abiertos
Obtenidos el 2026-03-02

Se analizará por medio de las apis proporcionadas únicamente.
'''

import pandas
import requests

dimensiones_financiamiento = 'organismo,grupo_organismo,rango_salarial,valor_vivienda,tipo_credito,modalidad'
dimensiones_conavi = 'rango_edad,rango_salarial,tipo_vivienda,valor_vivienda,modalidad'
dimensiones_FOVISSSTE = 'rango_edad,rango_salarial,valor_vivienda,modalidad'
dimensiones_infonavit = 'rango_edad,rango_salarial,valor_vivienda,vivienda,modalidad'
dimensiones_CNBV = 'rango_edad,rango_salarial,valor_vivienda,modalidad'
dimensiones_inv_vivienda = 'avance_obra,segmento_uma,tipo_vivienda,pcu,segmento'

class API_gob_vivienda_builder():
    años = '2025'
    clave_estado = '09'
    clave_municipio = '014'
    url : str
    df : pandas.DataFrame

    def __init__(self, Get_Function : str, dimensiones : str):
        self.dimensiones = dimensiones
        params=f"{Get_Function}/{self.años}/{self.clave_estado}/{self.clave_municipio}/{dimensiones}"
        self.url=f"https://sniiv.sedatu.gob.mx/api/CuboAPI/{params}"
        r = requests.get(self.url)
        print(r.status_code)
        self.df = self.gen_df(r)
        if self.df.empty:
           print("Dataframe is empty\n\tExiting...")
           exit(1)
        pass

    def export_to_csv(self, nombre_CSV : str):
        self.df.to_csv(f"{nombre_CSV}.csv", index=False)
        print("Exported to CSV")
        pass

    def __repr__(self) -> str:
        return self.url 

    def gen_df(self, r : requests.models.Response) -> pandas.DataFrame:
        return pandas.DataFrame(r.json())

'''
############# END OF FACTORY FUNCTION #############
'''

Financiamiento = API_gob_vivienda_builder("GetFinanciamiento",dimensiones_financiamiento)
Financiamiento.export_to_csv("Financiamiento")
CONAVI = API_gob_vivienda_builder("GetCONAVI",dimensiones_conavi)
CONAVI.export_to_csv("CONAVI")
FOVISSSTE = API_gob_vivienda_builder("GetFOVISSSTE",dimensiones_FOVISSSTE)
FOVISSSTE.export_to_csv("FOVISSSTE")
INFONAVIT = API_gob_vivienda_builder("GetINFONAVIT",dimensiones_infonavit)
INFONAVIT.export_to_csv("INFONAVIT")
CNBV = API_gob_vivienda_builder("GetCNBV",dimensiones_CNBV)
CNBV.export_to_csv("CNBV")
Inventario_de_vivienda = API_gob_vivienda_builder("GetInventario",dimensiones_inv_vivienda)
Inventario_de_vivienda.export_to_csv("Inventario_de_vivienda")


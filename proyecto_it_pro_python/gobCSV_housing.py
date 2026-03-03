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
dimensiones_reg_vivienda = 'segmento,segmento_uma,tipo_vivienda,superficie,recamara'
dimensiones_verificacion = 'segmento,segmento_uma,tipo_vivienda,superficie,recamara'
dimensiones_produccion = 'segmento,segmento_uma,tipo_vivienda,superficie,recamara'

'''
############## END OF PARAMETER SETTING ###############
'''
############## FACTORY FOR API CLASS ################

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
           print(f"Dataframe {Get_Function} is empty\n\tExiting...")
           return
        else:
            self.export_to_csv(Get_Function)
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
############# START OF API CSV GENERATION #########
Financiamiento = API_gob_vivienda_builder("GetFinanciamiento",dimensiones_financiamiento)
CONAVI = API_gob_vivienda_builder("GetCONAVI",dimensiones_conavi)
FOVISSSTE = API_gob_vivienda_builder("GetFOVISSSTE",dimensiones_FOVISSSTE)
INFONAVIT = API_gob_vivienda_builder("GetINFONAVIT",dimensiones_infonavit)
CNBV = API_gob_vivienda_builder("GetCNBV",dimensiones_CNBV)
Inventario_de_vivienda = API_gob_vivienda_builder("GetInventario",dimensiones_inv_vivienda)
Registro_de_vivienda = API_gob_vivienda_builder("GetRegistro",dimensiones_reg_vivienda)
Verificacion_de_vivienda = API_gob_vivienda_builder("GetVerificacion",dimensiones_verificacion)
Produccion_de_vivienda = API_gob_vivienda_builder("GetProduccion",dimensiones_produccion)

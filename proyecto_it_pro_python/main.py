
'''
1. Recopilar y clasificar los datos de apis o precios 
de materiales, mano de obra, etc.

Guardar porcentajes de costos y variables de precios. Como JSON, CSV y XML

2. Crear un modelo de almacenamiento de datos.

3. Gráficas.
'''

dimensiones_financiamiento = 'organismo,grupo_organismo,rango_salarial,valor_vivienda,tipo_credito,modalidad'
dimensiones_conavi = 'rango_edad,rango_salarial,tipo_vivienda,valor_vivienda,modalidad'
dimensiones_FOVISSSTE = 'rango_edad,rango_salarial,valor_vivienda,modalidad'
dimensiones_infonavit = 'rango_edad,rango_salarial,valor_vivienda,vivienda,modalidad'
dimensiones_CNBV = 'rango_edad,rango_salarial,valor_vivienda,modalidad'
dimensiones_inv_vivienda = 'avance_obra,segmento_uma,tipo_vivienda,pcu,segmento'
dimensiones_reg_vivienda = 'segmento,segmento_uma,tipo_vivienda,superficie,recamara'
dimensiones_verificacion = 'segmento,segmento_uma,tipo_vivienda,superficie,recamara'
dimensiones_produccion = 'segmento,segmento_uma,tipo_vivienda,superficie,recamara'


import pandas as pd
import gobCSV_housing as ghCSV
import json


def housing_costs():
    segmento_uma : str
    segmento : str
    superficie : str
    recamara : str
    pcu : str
    tipo_vivienda : str
    modalidad : str
    valor_vivienda : str 
    avance_obra : str
    pass

# El parseo demográfico podemos aproximarlo sabiendo que la población en 
# la Benito Juárez oscila alrededor de 400,000 habitantes. De esto, tenemos 
# que tomar en cuenta el porcentaje de esa población que es Económicamente Activa
# y relacionarlo dentro de las tablas csv's, que ofrecen la cantidad de nuevas viviendas
# construidas por su respectivo rango de edad. Sabiendo esto, podemos unir al 
# modelo de crecimiento por edad, y, así, su demanda a los años aproximados.

# La ecuación
# Pop(time) = pop_actual.edad + time +(-) f_incremento/decremento_pop(edad) 

def demographic_parse():
    rango_edad : str
    rango_salarial : str
    pass

# PARSE DATAFRAMES ON HOUSING COSTS 
def calc_costos_construccion():
    housing_costs()
    pass

# MATH
def costo_final():
    pass

# MATH
def ganancia_total():
    pass

def ofertaDemanda():
    demographic_parse()
    pass

def incertidumbre():
    pass



############# START OF API CSV GENERATION #########
Financiamiento = ghCSV.API_gob_vivienda_builder("GetFinanciamiento",dimensiones_financiamiento)
CONAVI = ghCSV.API_gob_vivienda_builder("GetCONAVI",dimensiones_conavi)
FOVISSSTE = ghCSV.API_gob_vivienda_builder("GetFOVISSSTE",dimensiones_FOVISSSTE)
INFONAVIT = ghCSV.API_gob_vivienda_builder("GetINFONAVIT",dimensiones_infonavit)
CNBV = ghCSV.API_gob_vivienda_builder("GetCNBV",dimensiones_CNBV)
Inventario_de_vivienda = ghCSV.API_gob_vivienda_builder("GetInventario",dimensiones_inv_vivienda)
Registro_de_vivienda = ghCSV.API_gob_vivienda_builder("GetRegistro",dimensiones_reg_vivienda)
Verificacion_de_vivienda = ghCSV.API_gob_vivienda_builder("GetVerificacion",dimensiones_verificacion)
Produccion_de_vivienda = ghCSV.API_gob_vivienda_builder("GetProduccion",dimensiones_produccion)
############ END OF API CSV GENERATION #########

# Costo(tipo-de-vivienda, tiempo) = f_costo(tipo_de_vivienda,tiempo) + f_costo_demanda(tipo_de_vivienda,tiempo)

# f_costo(tipo_de_vivienda,tiempo) = tipo_de_vivienda(vertical/horizontal,var_precios,m2)

# f_costo_demanda = pop_growth(non-linear,non-exponencial,non-recursive)---f(rango_de_edades)*PEA---cantidad de 
#                       gente @gente que sera parte o es de la PEA
# f_costo_vivienda = P(no_de_casas) + Incremento_m2
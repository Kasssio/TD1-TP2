from campana_verde import CampanaVerde
import csv

class DataSetCampanasVerdes:
    def __init__(self, archivo_csv:str):
        ''' completar docstring '''
        f = open(archivo_csv,"r",encoding="utf-8")
        campanas:list[CampanaVerde] = []
        for linea in csv.DictReader(f):
            dir:str = linea['direccion']
            bar:str = linea['barrio']
            com:int = int(linea['comuna'])
            mats:set = set(linea['materiales'].split(' / '))
            punto:list[str] = linea['WKT'].split(' ')
            lat:float = float(punto[1][1:])
            lon:float = float(punto[2][:-1])
            camp = CampanaVerde(dir, bar, com, mats, lat, lon)
            campanas.append(camp)
        print(campanas)

    # def tamano(...) -> ...:
    #     ''' completar docstring '''
    #     pass

    # def barrios(...) -> ...:
    #     ''' completar docstring '''
    #     pass

    # def campanas_del_barrio(...) -> ...:
    #     ''' completar docstring '''
    #     pass

    # def cantidad_por_barrio(...) -> ...:
    #     ''' completar docstring '''
    #     pass

    # def tres_campanas_cercanas(...) -> ...:
    #     ''' completar docstring '''
    #     pass

    # def exportar_por_materiales(...) -> ...:
    #     ''' completar docstring '''
    #     pass

# hola = 'POINT (-58.4436445327415 -34.5893377789048)'
# print (hola.split(' ')
dataset = DataSetCampanasVerdes('campanas-verdes.csv')
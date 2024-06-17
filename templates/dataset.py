from campana_verde import CampanaVerde
import csv

class DataSetCampanasVerdes:
    def __init__(self, archivo_csv:str):
        '''
        Inicializa un dataset con una lista de campanas verdes en base a un archivo csv.
        Requiere: el nombre de un archivo de extensión csv.
        '''
        f = open(archivo_csv, encoding='utf-8') # Abrimos el CSV con UTF-8 para que tome los acentos
        self.campanas:list[CampanaVerde] = []
        for linea in csv.DictReader(f, delimiter=';'): # Lee el CSV como un conjunto de diccionarios, con las claves delimitadas por ;
            dir:str = linea['direccion']
            bar:str = linea['barrio']
            com:int = int(linea['comuna'])
            mats:set = set(linea['materiales'].split(' / '))
            punto:list[str] = linea['WKT'].split(' ')
            lat:float = float(punto[1][1:])
            lon:float = float(punto[2][:-1])
            camp = CampanaVerde(dir, bar, com, mats, lat, lon) # Importante que los parámetros sigan el orden de la clase
            self.campanas.append(camp)

    def tamano(self) -> int:
        '''
        Requiere: nada.
        Devuelve: la cantidad de campanas del dataset.
        '''
        return len(self.campanas) #O(N)

    def barrios(self) -> set[str]:
        '''
        Requiere: nada.
        Devuelve: el conjunto de todos los barrios del dataset.
        '''
        barrios:set[str] = {} #NO ANDA, CORREGIR
        for campana in self.campanas:
            barrios.add(campana['barrio'])
        return barrios

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
print(dataset.barrios())
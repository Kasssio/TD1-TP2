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

    def ordenar_por_distancia(camps_cerca:list[CampanaVerde],lat:float,lon:float): #función auxiliar
        if (camps_cerca[0].distancia(lat,lon) > camps_cerca[1].distancia(lat,lon)):
            camps_cerca[0], camps_cerca[1] = camps_cerca[1], camps_cerca[0]
        if (camps_cerca[0].distancia(lat,lon) > camps_cerca[2].distancia(lat,lon)):
            camps_cerca[0], camps_cerca[2] = camps_cerca[2], camps_cerca[0]
        if (camps_cerca[1].distancia(lat,lon) > camps_cerca[2].distancia(lat,lon)):
            camps_cerca[1], camps_cerca[2] = camps_cerca[2], camps_cerca[1]

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
        barrios:set[str] = set() 
        for campana in self.campanas: # Complejidad O(N)
            barrios.add(campana.barrio) # Complejidad O(B), consultar por foro o profe
        return barrios

    def campanas_del_barrio(self,barrio:str) -> list[CampanaVerde]:
        ''' 
        Requiere: nada.
        Devuelve: La cantidad de campanas verdes en un barrio.
        '''
        barrio = barrio.upper()
        vr:list[CampanaVerde] = []
        for campana in self.campanas:
            if campana.barrio == barrio:
                vr.append(campana)
        return vr

    def cantidad_por_barrio(self,material) -> dict[str,int]:
        ''' 
        Requiere: nada.
        Devuelve: un diccionario con la cantidad de campanas verdes en un barrio en las que se puede depositar material.
        '''
        vr:dict[str,int] = {}
        barrios = self.barrios()
        for barrio in barrios:
            vr[barrio] = 0
            campanas = self.campanas_del_barrio(barrio)
            for i in campanas:
                if material in i.materiales:
                    vr[barrio] += 1
        return vr

    def tres_campanas_cercanas(self,lat,lon) -> tuple[CampanaVerde,CampanaVerde,CampanaVerde]:
        '''
        Requiere: Nada.
        Devuelve: las tres campanas más cerca de la ubicación dada.
        '''
        # HACERLO CON LISTAS
        # Primero codifico los casos para los cuales el dataset contiene más de 3 campanas
        # Arranco desde las 3 primeras campanas
        camps_cerca:list[CampanaVerde] = []
        for i in range(3):
            camps_cerca.append(self.campanas[i])
        # Ordeno las 3 primeras campanas
        # for campana in self.campanas: # æ
        # Ahora voy añadiendo las campanas restantes del dataset, en orden
        # TERMINAR URGENTE

    def exportar_por_materiales(self, archivo_csv:str, materiales:set) -> ...:
        '''  genera un nuevo archivo con
        nombre archivo_csv que contiene las campanas verdes en el dataset d en las que se pueda
        depositar todos los materiales del conjunto materiales, conjunto indicado como input del
        método. El archivo generado contiene únicamente las columnas DIRECCION y BARRIO .
        '''
        f = open(archivo_csv, 'w', encoding='utf-8')
        f.write("DIRECCION;BARRIO\n")
        for campana in self.campanas:
            if materiales & campana.materiales == materiales:
                f.write(campana.direccion + ";" + campana.barrio + "\n")


# hola = 'POINT (-58.4436445327415 -34.5893377789048)'
# print (hola.split(' ')
dataset = DataSetCampanasVerdes('templates/csv-test.csv')
print(dataset.cantidad_por_barrio('Vidrio'))
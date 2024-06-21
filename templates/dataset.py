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
        return len(self.campanas) #O(1)

    def barrios(self) -> set[str]:
        '''
        Requiere: nada.
        Devuelve: el conjunto de todos los barrios del dataset.
        '''
        barrios:set[str] = set() 
        for campana in self.campanas: # Complejidad O(N)
            barrios.add(campana.barrio) # Complejidad O(B)
        return barrios

    def campanas_del_barrio(self,barrio:str) -> list[CampanaVerde]:
        ''' 
        Requiere: nada.
        Devuelve: Una lista que contiene todas las campanas verdes en el barrio indicado.
        '''
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
            for campana in campanas:
                if material in campana.materiales:
                    vr[barrio] += 1
        return vr
    
    def ordenar_lista_de_tres(self,campana:CampanaVerde,lista:list[CampanaVerde],lat:float,lon:float):
        '''
        Requiere: len(lista) = 3.
        Devuelve: una lista de 3 campanas ordenadas en base a su cercanía a una coordenada.
        '''
        if (lista[0].distancia(lat,lon) > campana.distancia(lat,lon)):
            lista[0], lista[1], lista[2] = campana, lista[0], lista[1]
        elif (lista[1].distancia(lat,lon) > campana.distancia(lat,lon)):
            lista[1], lista[2] = campana, lista[1]
        elif (lista[2].distancia(lat,lon) > campana.distancia(lat,lon)):
            lista[2] = campana

    def tres_campanas_cercanas(self,lat:float,lon:float) -> tuple[CampanaVerde,CampanaVerde,CampanaVerde]:
        '''
        Requiere: Nada.
        Devuelve: las tres campanas más cerca de la ubicación dada.
        '''
        # Armo una lista con las primeras tres campanas del dataset
        camps_cerca:list[CampanaVerde] = []
        for i in range(3):
            camps_cerca.append(self.campanas[i])
        # Ordeno la lista
        if (camps_cerca[0].distancia(lat,lon) > camps_cerca[1].distancia(lat,lon)):
            camps_cerca[0], camps_cerca[1] = camps_cerca[1], camps_cerca[0]
        if (camps_cerca[0].distancia(lat,lon) > camps_cerca[2].distancia(lat,lon)):
            camps_cerca[0], camps_cerca[2] = camps_cerca[2], camps_cerca[0]
        if (camps_cerca[1].distancia(lat,lon) > camps_cerca[2].distancia(lat,lon)):
            camps_cerca[1], camps_cerca[2] = camps_cerca[2], camps_cerca[1]
        for campana in self.campanas: # Voy agregando a la lista campanas más cercanas
            self.ordenar_lista_de_tres(campana, camps_cerca, lat, lon)
        return camps_cerca
    
    def exportar_por_materiales(self, archivo_csv:str, materiales:set):
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

dataset = DataSetCampanasVerdes('TD1-TP2/templates/campanas-verdes.csv')

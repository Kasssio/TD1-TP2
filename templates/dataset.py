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
            # A continuación inicializamos todas las variables
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
        # Simplemente debo sacar la longitud de self.campanas, que contiene todas las campanas del dataset
        return len(self.campanas)

    def barrios(self) -> set[str]:
        '''
        Requiere: nada.
        Devuelve: el conjunto de todos los barrios del dataset.
        '''
        barrios:set[str] = set() # Inicializo el conjunto
        for campana in self.campanas: # Por cada campana
            barrios.add(campana.barrio) # Añado su barrio al conjunto (no se repiten gracias a las propiedades de los conjuntos)
        return barrios # Devuelvo el conjunto de barrios

    def campanas_del_barrio(self,barrio:str) -> list[CampanaVerde]:
        ''' 
        Requiere: nada.
        Devuelve: una lista con las campanas verdes que hay en un barrio.
        '''
        vr:list[CampanaVerde] = [] # Acá se guardarán las campanas
        for campana in self.campanas: # Por cada campana del dataset
            if campana.barrio == barrio: # Si la campana pertenece a ese barrio...
                vr.append(campana) # ...la añadimos a la lista!
        return vr

    def cantidad_por_barrio(self,material) -> dict[str,int]:
        ''' 
        Requiere: nada.
        Devuelve: un diccionario con la cantidad de campanas verdes en un barrio en las que se puede depositar material.
        '''
        vr:dict[str,int] = {} # Iniciamos un diccionario donde a cada barrio le asociamos la cantidad de campanas en las cuales podemos poner el material especificado
        barrios = self.barrios() # Guardamos los barrios existentes en el dataset
        for barrio in barrios: # Por cada barrio
            vr[barrio] = 0 # Creamos su clave en el diccionario
            campanas = self.campanas_del_barrio(barrio) # Extraemos todas las campanas presentes en ese barrio
            for campana in campanas: # Por cada una de esas campanas
                if material in campana.materiales: #Si en esa campana se puede tirar el material especificado
                    vr[barrio] += 1 # Agregamos una campana al contador
        return vr # Devolvemos el diccionario
    
    def ordenar_lista_de_tres(self,campana:CampanaVerde,lista:list[CampanaVerde],lat:float,lon:float):
        '''
        Requiere: len(lista) = 3.
        Devuelve: una lista de 3 campanas ordenadas en base a su cercanía a una coordenada.
        '''
        if (lista[0].distancia(lat,lon) > campana.distancia(lat,lon)): # Si la campana actual tiene una distancia menor a la primera campana de la lista
            lista[0], lista[1], lista[2] = campana, lista[0], lista[1] # La pone como primer elemento y mueve las demás campanas una posición hacia la derecha
        elif (lista[1].distancia(lat,lon) > campana.distancia(lat,lon)): # Si la campana actual tiene una distancia mayor a la primera pero menor a la segunda
            lista[1], lista[2] = campana, lista[1] # La pone como segundo elemento y mueve la siguiente campana una posición hacia la derecha
        elif (lista[2].distancia(lat,lon) > campana.distancia(lat,lon)): # Si la campana actual tiene una distancia que es menor sólamente a la de la última
            lista[2] = campana # Reemplaza la última posición por la campana actual

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
        for campana in self.campanas: # Por cada campana en el dataset
            self.ordenar_lista_de_tres(campana, camps_cerca, lat, lon) # Llamo a la función que definí antes para ordenarla dentro de la lista
        return camps_cerca # Devuelve las campanas cercanas
    
    def exportar_por_materiales(self, archivo_csv:str, materiales:set):
        '''  genera un nuevo archivo con
        nombre archivo_csv que contiene las campanas verdes en el dataset d en las que se pueda
        depositar todos los materiales del conjunto materiales, conjunto indicado como input del
        método. El archivo generado contiene únicamente las columnas DIRECCION y BARRIO .
        '''
        f = open(archivo_csv, 'w', encoding='utf-8') # Abro un archivo nuevo
        f.write("DIRECCION;BARRIO\n") # Le agrego el encabezado para identificar cada columna
        for campana in self.campanas: # Por cada campana del dataset
            if materiales & campana.materiales == materiales: # Si en esa campana se pueden tirar todos los materiales especificados
                f.write(campana.direccion + ";" + campana.barrio + "\n") # La añadimos al archivo

dataset = DataSetCampanasVerdes('TD1-TP2/templates/csv-test.csv')
print(dataset.tres_campanas_cercanas(-58.4427816117563,-34.5873114041397))


import unittest
import csv

# Importamos el codigo a testear.
from dataset import DataSetCampanasVerdes
from campana_verde import CampanaVerde

# Inicializamos datasets para testear
d1:DataSetCampanasVerdes = DataSetCampanasVerdes('templates/csv-test.csv') # Estos tres datasets dependen de un path relativo, si no funciona durante la corrección cambiar el directorio del csv.
d2:DataSetCampanasVerdes = DataSetCampanasVerdes('templates/campanas-verdes.csv')
d3:DataSetCampanasVerdes = DataSetCampanasVerdes('templates/csv-vacio.csv')
d4:DataSetCampanasVerdes = DataSetCampanasVerdes('templates/csv-test-2c.csv')
print(len(d4.campanas))

# Inicializamos algunas variables que nos van a servir para testear
campsBalvanera:list[CampanaVerde] = d1.campanas_del_barrio('BALVANERA')
campsBalvaneraSTR:list[str] = ['<MORENO 1889@Cartón/Metal/Papel/Plástico/Vidrio@BALVANERA>', '<MORENO 2037@Cartón/Metal/Papel/Plástico/Vidrio@BALVANERA>', '<MORENO 2277@Cartón/Metal/Papel/Plástico/Vidrio@BALVANERA>', '<MORENO 2415@Cartón/Metal/Papel/Plástico/Vidrio@BALVANERA>', '<MORENO 2679@Cartón/Metal/Papel/Plástico/Vidrio@BALVANERA>', '<MORENO 3015@Cartón/Metal/Papel/Plástico/Vidrio@BALVANERA>', '<MORENO 3219@Cartón/Metal/Papel/Plástico/Vidrio@BALVANERA>', '<SARMIENTO 1935@Cartón/Metal/Papel/Plástico/Vidrio@BALVANERA>', '<SARMIENTO 2125@Cartón/Metal/Papel/Plástico/Vidrio@BALVANERA>', '<SARMIENTO 2959@Cartón/Metal/Papel/Plástico/Vidrio@BALVANERA>', '<SARMIENTO 3333@Cartón/Metal/Papel/Plástico/Vidrio@BALVANERA>']
campsCerca0:tuple[CampanaVerde,CampanaVerde,CampanaVerde] = ['<CASTILLO 1538@Cartón/Metal/Papel/Plástico/Vidrio@CHACARITA>', '<CASTILLO 1748@Cartón/Metal/Papel/Plástico/Vidrio@CHACARITA>', '<CASTILLO 1302@Cartón/Metal/Papel/Plástico/Vidrio@CHACARITA>']
tresCamps0:tuple[CampanaVerde,CampanaVerde,CampanaVerde] = d1.tres_campanas_cercanas(-58.4427816117563,-34.5873114041397)
campsCerca1:tuple[CampanaVerde, CampanaVerde] = ['<MENDOZA 2132@Cartón/Papel@BELGRANO>', '<REMEDIOS 3715@Cartón/Metal/Papel/Plástico/Vidrio@PARQUE AVELLANEDA>']
tresCamps1:tuple[CampanaVerde, CampanaVerde] = d4.tres_campanas_cercanas(-58.4427816117563,-34.5873114041397)

class TestDataSetCampanasVerdes(unittest.TestCase):

    def test_init(self):
        self.assertNotEqual(d1,None) # Chequeamos que el dataset se cree correctamente, es decir, que no sea None


    def test_tamano(self): # Testeamos la función que devuelve la cantidad de campanas de un dataset
        self.assertEqual(d1.tamano(), 121) # Probamos con tamaños chicos
        self.assertEqual(d2.tamano(), 2974) # Probamos con tamaños grandes y con líneas en blanco (este archivo tiene una línea en blanco al final)
        self.assertEqual(d3.tamano(), 0)

    def test_barrios(self): # Testeamos la función que devuelve los barrios contenidos en el dataset
        # Probamos con un dataset con pocos barrios
        self.assertEqual(d1.barrios(), {'ALMAGRO', 'LINIERS', 'COLEGIALES', 'VILLA ORTUZAR', 'MONTE CASTRO', 'VILLA URQUIZA', 'VILLA CRESPO', 'PUERTO MADERO', 'NUÑEZ', 'PARQUE PATRICIOS', 'CHACARITA', 'MONSERRAT', 'PALERMO', 'NUEVA POMPEYA', 'BARRACAS', 'BELGRANO', 'BOCA', 'CONSTITUCION', 'BALVANERA', 'SAN CRISTOBAL', 'PARQUE AVELLANEDA', 'VILLA SOLDATI', 'FLORES', 'SAAVEDRA', 'BOEDO', 'CABALLITO', 'VILLA DEVOTO', 'SAN NICOLAS', 'VILLA RIACHUELO'})
        # Probamos con un dataset con muchos barrios
        self.assertEqual(d2.barrios(), {'SAN NICOLAS', 'SAN TELMO', 'VILLA ORTUZAR', 'MONTE CASTRO', 'CABALLITO', 'VILLA SANTA RITA', 'PUERTO MADERO', 'VILLA LURO', 'NUÑEZ', 'COGHLAN', 'BELGRANO', 'VILLA DEVOTO', 'PARQUE PATRICIOS', 'AGRONOMIA', 'VILLA CRESPO', 'PARQUE AVELLANEDA', 'FLORESTA', 'MONSERRAT', 'VILLA SOLDATI', 'CHACARITA', 'VERSALLES', 'LINIERS', 'MATADEROS', 'SAAVEDRA', 'VILLA DEL PARQUE', 'FLORES', 'CONSTITUCION', 'VELEZ SARSFIELD', 'VILLA REAL', 'PALERMO', 'SAN CRISTOBAL', 'BARRACAS', 'VILLA URQUIZA', 'PATERNAL', 'COLEGIALES', 'VILLA LUGANO', 'PARQUE CHAS', 'RECOLETA', 'VILLA RIACHUELO', 'VILLA PUEYRREDON', 'PARQUE CHACABUCO', 'BALVANERA', 'BOCA', 'VILLA GENERAL MITRE', 'NUEVA POMPEYA', 'BOEDO', 'RETIRO', 'VILLA GRAL. MITRE', 'ALMAGRO'})
    
    def test_campanas_del_barrio(self):
        self.maxDiff = None
        for i in range(len(campsBalvanera)): # Convertimos todas las campanas verdes en str para poder compararlas con campsBarrio0
            campsBalvanera[i] = str(campsBalvanera[i])

        self.assertEqual(campsBalvanera, campsBalvaneraSTR) # Probamos con campanas que estén en Balvanera
        self.assertEqual(d1.campanas_del_barrio('MI CASA'),[]) # Probamos en pasarle un barrio que no existe en el dataset
    
    def test_cantidad_por_barrios(self): # Testeamos la función que devuelve la cantidad de campanas por barrio en las cuales se puede depositar el material especificado
        self.maxDiff = None
        # Probamos con un dataset lleno, con todos los materiales
        self.assertEqual(d1.cantidad_por_barrio('Cartón'), {'CABALLITO': 10, 'VILLA ORTUZAR': 7, 'ALMAGRO': 7, 'PARQUE PATRICIOS': 1, 'SAAVEDRA': 2, 'PARQUE AVELLANEDA': 4, 'BELGRANO': 6, 'VILLA RIACHUELO': 1, 'NUEVA POMPEYA': 2, 'VILLA CRESPO': 5, 'SAN NICOLAS': 4, 'MONSERRAT': 5, 'COLEGIALES': 2, 'VILLA SOLDATI': 1, 'CHACARITA': 9, 'PALERMO': 2, 'VILLA DEVOTO': 1, 'BOEDO': 6, 'FLORES': 7, 'NUÑEZ': 7, 'SAN CRISTOBAL': 2, 'MONTE CASTRO': 1, 'BARRACAS': 5, 'BALVANERA': 11, 'BOCA': 3, 'PUERTO MADERO': 1, 'LINIERS': 1, 'CONSTITUCION': 2, 'VILLA URQUIZA': 4})
        self.assertEqual(d1.cantidad_por_barrio('Metal'), {'PUERTO MADERO': 1, 'SAAVEDRA': 2, 'BELGRANO': 3, 'ALMAGRO': 7, 'PARQUE AVELLANEDA': 4, 'PARQUE PATRICIOS': 1, 'COLEGIALES': 2, 'VILLA URQUIZA': 4, 'SAN CRISTOBAL': 2, 'PALERMO': 2, 'FLORES': 7, 'BARRACAS': 5, 'NUÑEZ': 7, 'MONTE CASTRO': 0, 'CHACARITA': 9, 'BOEDO': 6, 'NUEVA POMPEYA': 2, 'SAN NICOLAS': 4, 'BOCA': 3, 'CONSTITUCION': 0, 'VILLA ORTUZAR': 7, 'BALVANERA': 11, 'VILLA DEVOTO': 0, 'MONSERRAT': 5, 'VILLA CRESPO': 0, 'LINIERS': 1, 'VILLA RIACHUELO': 1, 'VILLA SOLDATI': 1, 'CABALLITO': 10})
        self.assertEqual(d1.cantidad_por_barrio('Papel'), {'BALVANERA': 11, 'VILLA URQUIZA': 4, 'SAAVEDRA': 2, 'BARRACAS': 5, 'ALMAGRO': 7, 'SAN CRISTOBAL': 3, 'NUEVA POMPEYA': 2, 'CABALLITO': 10, 'SAN NICOLAS': 4, 'FLORES': 7, 'MONTE CASTRO': 1, 'VILLA CRESPO': 5, 'LINIERS': 1, 'PARQUE AVELLANEDA': 4, 'BOCA': 4, 'MONSERRAT': 5, 'PARQUE PATRICIOS': 1, 'COLEGIALES': 2, 'VILLA RIACHUELO': 1, 'CONSTITUCION': 2, 'NUÑEZ': 7, 'BOEDO': 6, 'VILLA ORTUZAR': 7, 'VILLA SOLDATI': 1, 'BELGRANO': 6, 'VILLA DEVOTO': 1, 'CHACARITA': 9, 'PUERTO MADERO': 1, 'PALERMO': 2})
        self.assertEqual(d1.cantidad_por_barrio('Plástico'), {'COLEGIALES': 2, 'CONSTITUCION': 0, 'VILLA URQUIZA': 4, 'BELGRANO': 3, 'NUÑEZ': 7, 'PARQUE PATRICIOS': 1, 'FLORES': 7, 'BARRACAS': 5, 'BALVANERA': 11, 'SAAVEDRA': 2, 'PUERTO MADERO': 1, 'VILLA ORTUZAR': 7, 'NUEVA POMPEYA': 2, 'SAN NICOLAS': 4, 'SAN CRISTOBAL': 2, 'ALMAGRO': 7, 'CHACARITA': 9, 'MONSERRAT': 5, 'PARQUE AVELLANEDA': 4, 'LINIERS': 1, 'BOEDO': 6, 'PALERMO': 2, 'VILLA DEVOTO': 0, 'BOCA': 3, 'VILLA SOLDATI': 1, 'VILLA RIACHUELO': 1, 'CABALLITO': 10, 'MONTE CASTRO': 0, 'VILLA CRESPO': 0})
        self.assertEqual(d1.cantidad_por_barrio('Vidrio'), {'BARRACAS': 5, 'COLEGIALES': 2, 'MONTE CASTRO': 0, 'CHACARITA': 9, 'SAN NICOLAS': 4, 'PARQUE PATRICIOS': 1, 'BALVANERA': 11, 'VILLA SOLDATI': 1, 'VILLA CRESPO': 0, 'SAN CRISTOBAL': 2, 'SAAVEDRA': 2, 'NUEVA POMPEYA': 2, 'VILLA URQUIZA': 4, 'BOCA': 3, 'ALMAGRO': 7, 'CONSTITUCION': 0, 'FLORES': 7, 'CABALLITO': 10, 'NUÑEZ': 7, 'PALERMO': 2, 'BOEDO': 6, 'LINIERS': 1, 'PARQUE AVELLANEDA': 4, 'MONSERRAT': 5, 'VILLA DEVOTO': 0, 'BELGRANO': 3, 'PUERTO MADERO': 1, 'VILLA ORTUZAR': 7, 'VILLA RIACHUELO': 1})
        # Probamos con una 
        self.assertEqual(d3.cantidad_por_barrio('Cartón'), {})
        self.assertEqual(d3.cantidad_por_barrio('Metal'), {})
        self.assertEqual(d3.cantidad_por_barrio('Papel'), {})
        self.assertEqual(d3.cantidad_por_barrio('Plástico'), {})
        self.assertEqual(d3.cantidad_por_barrio('Vidrio'), {})

    def test_tres_campanas_cercanas(self):
        for i in range(3):
            tresCamps0[i] = str(tresCamps0[i]) # Para que el intérprete no tire error, lo pasamos a string
        for i in range(2):
            tresCamps1[i] = str(tresCamps1[i]) # Para que el intérprete no tire error, lo pasamos a string
        self.assertEqual(tresCamps0,campsCerca0) # Probamos el funcionamiento para un dataset de 2 campanas
        self.assertEqual(tresCamps1, campsCerca1) # Probamos el funcionamiento para un dataset de 3 o más


    def test_exportar_muchas_campanas(self):
        fileToRead:DataSetCampanasVerdes = d1 # Llamamos un dataset
        fileExport:str = 'templates/csv-exporter.csv' # Este archivo es el destino de exportar_por_materiales
        material:set[str] = {'Papel'}
        fileToRead.exportar_por_materiales(fileExport,material)
        result:str = 'templates/csv-exporter.csv'
        expected:str = 'templates/expected-csv.csv' # Este csv contiene los contenidos esperados del resultado
        f = open(result, encoding='utf-8') 
        g = open(expected, encoding='utf-8')
        a:str = f.read() # Pasamos los contenidos a tipo str para facilitar la comparación
        b:str = g.read()
        self.assertEqual(a,b)
        f.close()
        g.close()
        
    def test_exportar_cero_campanas(self):
        fileToRead:DataSetCampanasVerdes = d1 # Llamamos un dataset 
        fileExport:str = 'templates/csv-exporter.csv' # Este archivo es el destino de exportar_por_materiales
        material:set[str] = {'Hola'}
        fileToRead.exportar_por_materiales(fileExport,material)
        result:str = 'templates/csv-exporter.csv'
        expected:str = 'templates/empty-export.csv' # Este csv está vacío, buscamos que pase esto
        f = open(result, encoding='utf-8') # Abrimos los dos archivos 
        g = open(expected, encoding='utf-8')
        a = f.read() # Pasamos los contenidos a tipo str para facilitar la comparación
        b = g.read()
        self.assertEqual(a,b)
        f.close()
        g.close()
unittest.main()
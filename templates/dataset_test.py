import unittest

# Importamos el codigo a testear.
from dataset import DataSetCampanasVerdes
from campana_verde import CampanaVerde

d1 = DataSetCampanasVerdes('TD1-TP2/templates/csv-test.csv') # Estos tres dicts dependen de un path relativo, si no funciona durante la corrección cambiar el directorio del csv.
d2 = DataSetCampanasVerdes('TD1-TP2/templates/campanas-verdes.csv')
d3 = DataSetCampanasVerdes('TD1-TP2/templates/csv-test2.csv')

campsBarrio0:list[CampanaVerde] = ['<MORENO 1889@Cartón/Metal/Papel/Plástico/Vidrio@BALVANERA>', '<MORENO 2037@Cartón/Metal/Papel/Plástico/Vidrio@BALVANERA>', '<MORENO 2277@Cartón/Metal/Papel/Plástico/Vidrio@BALVANERA>', '<MORENO 2415@Cartón/Metal/Papel/Plástico/Vidrio@BALVANERA>', '<MORENO 2679@Cartón/Metal/Papel/Plástico/Vidrio@BALVANERA>', '<MORENO 3015@Cartón/Metal/Papel/Plástico/Vidrio@BALVANERA>', '<MORENO 3219@Cartón/Metal/Papel/Plástico/Vidrio@BALVANERA>', '<SARMIENTO 1935@Cartón/Metal/Papel/Plástico/Vidrio@BALVANERA>', '<SARMIENTO 2125@Cartón/Metal/Papel/Plástico/Vidrio@BALVANERA>', '<SARMIENTO 2959@Cartón/Metal/Papel/Plástico/Vidrio@BALVANERA>', '<SARMIENTO 3333@Cartón/Metal/Papel/Plástico/Vidrio@BALVANERA>']
campsBarrio1:list[CampanaVerde] = []

class TestDataSetCampanasVerdes(unittest.TestCase):

    def test_init(self):
        pass

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
        self.assertEqual(d1.campanas_del_barrio('BALVANERA'),...)
        pass
    
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

unittest.main()
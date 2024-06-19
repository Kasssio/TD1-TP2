import unittest

# Importamos el codigo a testear.
from dataset import DataSetCampanasVerdes

d1 = DataSetCampanasVerdes('templates/csv-test.csv')
d2 = DataSetCampanasVerdes('templates/campanas-verdes.csv')

class TestDataSetCampanasVerdes(unittest.TestCase):

    def test_tamano(self): # Testeamos la función que devuelve la cantidad de camapanas de un dataset
        self.assertEqual(d1.tamano(), 121) # Probamos con tamaños chicos
        self.assertEqual(d2.tamano(), 2974) # Probamos con tamaños grandes y con líneas en blanco (este archivo tiene una línea en blanco al final)

    def test_barrios(self): # Testeamos la función que devuelve los barrios contenidos en el dataset
        # Probamos con un dataset con pocos barrios
        self.assertEqual(d1.barrios(), {'ALMAGRO', 'LINIERS', 'COLEGIALES', 'VILLA ORTUZAR', 'MONTE CASTRO', 'VILLA URQUIZA', 'VILLA CRESPO', 'PUERTO MADERO', 'NUÑEZ', 'PARQUE PATRICIOS', 'CHACARITA', 'MONSERRAT', 'PALERMO', 'NUEVA POMPEYA', 'BARRACAS', 'BELGRANO', 'BOCA', 'CONSTITUCION', 'BALVANERA', 'SAN CRISTOBAL', 'PARQUE AVELLANEDA', 'VILLA SOLDATI', 'FLORES', 'SAAVEDRA', 'BOEDO', 'CABALLITO', 'VILLA DEVOTO', 'SAN NICOLAS', 'VILLA RIACHUELO'})
        # Probamos con un dataset con muchos barrios
        self.assertEqual(d2.barrios(), {'SAN NICOLAS', 'SAN TELMO', 'VILLA ORTUZAR', 'MONTE CASTRO', 'CABALLITO', 'VILLA SANTA RITA', 'PUERTO MADERO', 'VILLA LURO', 'NUÑEZ', 'COGHLAN', 'BELGRANO', 'VILLA DEVOTO', 'PARQUE PATRICIOS', 'AGRONOMIA', 'VILLA CRESPO', 'PARQUE AVELLANEDA', 'FLORESTA', 'MONSERRAT', 'VILLA SOLDATI', 'CHACARITA', 'VERSALLES', 'LINIERS', 'MATADEROS', 'SAAVEDRA', 'VILLA DEL PARQUE', 'FLORES', 'CONSTITUCION', 'VELEZ SARSFIELD', 'VILLA REAL', 'PALERMO', 'SAN CRISTOBAL', 'BARRACAS', 'VILLA URQUIZA', 'PATERNAL', 'COLEGIALES', 'VILLA LUGANO', 'PARQUE CHAS', 'RECOLETA', 'VILLA RIACHUELO', 'VILLA PUEYRREDON', 'PARQUE CHACABUCO', 'BALVANERA', 'BOCA', 'VILLA GENERAL MITRE', 'NUEVA POMPEYA', 'BOEDO', 'RETIRO', 'VILLA GRAL. MITRE', 'ALMAGRO'})
    
    def test_cantidad_por_barrios(self):
        pass

unittest.main()
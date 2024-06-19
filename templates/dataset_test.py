import unittest

# Importamos el codigo a testear.
from dataset import DataSetCampanasVerdes

####################################################################
d1 = DataSetCampanasVerdes('templates/csv-test.csv')
d2 = DataSetCampanasVerdes('templates/campanas-verdes.csv')

class TestDataSetCampanasVerdes(unittest.TestCase):

    def test_tamano(self):
        self.assertEqual(d1.tamano(), 121)
        self.assertEqual(d2.tamano(), 2974)

    def test_barrios(self):
        self.assertEqual(d1.barrios(), {'ALMAGRO', 'LINIERS', 'COLEGIALES', 'VILLA ORTUZAR', 'MONTE CASTRO', 'VILLA URQUIZA', 'VILLA CRESPO', 'PUERTO MADERO', 'NUÑEZ', 'PARQUE PATRICIOS', 'CHACARITA', 'MONSERRAT', 'PALERMO', 'NUEVA POMPEYA', 'BARRACAS', 'BELGRANO', 'BOCA', 'CONSTITUCION', 'BALVANERA', 'SAN CRISTOBAL', 'PARQUE AVELLANEDA', 'VILLA SOLDATI', 'FLORES', 'SAAVEDRA', 'BOEDO', 'CABALLITO', 'VILLA DEVOTO', 'SAN NICOLAS', 'VILLA RIACHUELO'})
        self.assertEqual(d2.barrios(), {'SAN NICOLAS', 'SAN TELMO', 'VILLA ORTUZAR', 'MONTE CASTRO', 'CABALLITO', 'VILLA SANTA RITA', 'PUERTO MADERO', 'VILLA LURO', 'NUÑEZ', 'COGHLAN', 'BELGRANO', 'VILLA DEVOTO', 'PARQUE PATRICIOS', 'AGRONOMIA', 'VILLA CRESPO', 'PARQUE AVELLANEDA', 'FLORESTA', 'MONSERRAT', 'VILLA SOLDATI', 'CHACARITA', 'VERSALLES', 'LINIERS', 'MATADEROS', 'SAAVEDRA', 'VILLA DEL PARQUE', 'FLORES', 'CONSTITUCION', 'VELEZ SARSFIELD', 'VILLA REAL', 'PALERMO', 'SAN CRISTOBAL', 'BARRACAS', 'VILLA URQUIZA', 'PATERNAL', 'COLEGIALES', 'VILLA LUGANO', 'PARQUE CHAS', 'RECOLETA', 'VILLA RIACHUELO', 'VILLA PUEYRREDON', 'PARQUE CHACABUCO', 'BALVANERA', 'BOCA', 'VILLA GENERAL MITRE', 'NUEVA POMPEYA', 'BOEDO', 'RETIRO', 'VILLA GRAL. MITRE', 'ALMAGRO'})
    
    def test_cantidad_por_barrios(self):
        pass

## y así con el resto de los métodos a testear.
        
####################################################################

unittest.main()
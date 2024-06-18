import unittest

# Importamos el codigo a testear.
from campana_verde import CampanaVerde

####################################################################
camp1:CampanaVerde = CampanaVerde('AGUIRRE 1447', 'CHACARITA', 15, {'Papel', 'Cartón'}, -58.4436445327415, -34.5893377789048)
camp2:CampanaVerde = CampanaVerde('CASTRO 1038', 'BOEDO', 5, {'Papel', 'Cartón', 'Plástico', 'Metal', 'Vidrio'}, -58.4203838859871, -34.6252247608196)
# POINT ( );;;Los materiales deben estar limpios y secos


class TestCampanaVerde(unittest.TestCase):
    # def test_repr(self):
    #     self.assertSetEqual(str(camp1), '<AGUIRRE 1447@Cartón/Papel@CHACARITA>')
    #     self.assertSetEqual(str(camp2), '<CASTRO 1038@Cartón/Metal/Papel/Plástico@BOEDO>')
        
    def test_distancia(self):
        self.assertEqual(camp1.distancia(0,0), 7169810.4462479055)
        self.assertEqual(camp1.distancia(-10,-1000), 10431466.276497768)
        self.assertEqual(camp1.distancia(1000,10), 2815979.0121014197)
        self.assertEqual(camp1.distancia(-10,1000), 6599505.7648359975)

## y asi con el resto de los metodos a testear.
        
####################################################################

unittest.main()

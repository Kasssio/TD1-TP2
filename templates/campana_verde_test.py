import unittest

# Importamos el codigo a testear.
from campana_verde import CampanaVerde

####################################################################
# POINT ( );;;Los materiales deben estar limpios y secos
dic1:dict[str,str,int,set,float,float] = {
    'direccion' : 'AGUIRRE 1447',
    'barrio' : 'CHACARITA',
    'comuna' : 15,
    'materiales' : {'Papel', 'Cartón'},
    'latitud' : -58.4436445327415, 
    'longitud' : -34.5893377789048
    }

dic2:dict[str,str,int,set,float,float] = {
    'direccion' : 'CASTRO 1038',
    'barrio' : 'BOEDO',
    'comuna' : 5,
    'materiales' : {'Papel', 'Cartón', 'Plástico', 'Metal', 'Vidrio'},
    'latitud' : -58.4203838859871, 
    'longitud' : -34.6252247608196
    }

camp1:CampanaVerde = CampanaVerde(dic1['direccion'], dic1['barrio'], dic1['comuna'], dic1['materiales'], dic1['latitud'], dic1['longitud'])
camp2:CampanaVerde = CampanaVerde(dic2['direccion'], dic2['barrio'], dic2['comuna'], dic2['materiales'], dic2['latitud'], dic2['longitud'])

class TestCampanaVerde(unittest.TestCase):
    def test_init(self):
        self.assertEqual(camp1.direccion, dic1['direccion'])
        self.assertEqual(camp1.barrio, dic1['barrio'])
        self.assertEqual(camp1.comuna, dic1['comuna'])
        self.assertEqual(camp1.materiales, dic1['materiales'])
        self.assertEqual(camp1.latitud, dic1['latitud'])
        self.assertEqual(camp1.longitud, dic1['longitud'])
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

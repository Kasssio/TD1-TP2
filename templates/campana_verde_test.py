import unittest

# Importamos el codigo a testear.
from campana_verde import CampanaVerde

####################################################################
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
    'materiales' : {'Papel', 'Cartón', 'Plástico', 'Metal'},
    'latitud' : -58.4203838859871, 
    'longitud' : -34.6252247608196
    }

dic3:dict[str,str,int,set,float,float] = {
    'direccion' : 'CASTRO 1038',
    'barrio' : 'BOEDO',
    'comuna' : 5,
    'materiales' : {},
    'latitud' : -58.4203838859871, 
    'longitud' : -34.6252247608196
    }

camp1:CampanaVerde = CampanaVerde(dic1['direccion'], dic1['barrio'], dic1['comuna'], dic1['materiales'], dic1['latitud'], dic1['longitud'])
camp2:CampanaVerde = CampanaVerde(dic2['direccion'], dic2['barrio'], dic2['comuna'], dic2['materiales'], dic2['latitud'], dic2['longitud'])
camp3:CampanaVerde = CampanaVerde(dic3['direccion'], dic3['barrio'], dic3['comuna'], dic3['materiales'], dic3['latitud'], dic3['longitud'])

class TestCampanaVerde(unittest.TestCase):
    def test_init(self):
        # Testeando el __init__ de la primera campana
        self.assertEqual(camp1.direccion, dic1['direccion'])
        self.assertEqual(camp1.barrio, dic1['barrio'])
        self.assertEqual(camp1.comuna, dic1['comuna'])
        self.assertEqual(camp1.materiales, dic1['materiales'])
        self.assertEqual(camp1.latitud, dic1['latitud'])
        self.assertEqual(camp1.longitud, dic1['longitud'])
        # Testeando el __init__ de la segunda campana
        self.assertEqual(camp2.direccion, dic2['direccion'])
        self.assertEqual(camp2.barrio, dic2['barrio'])
        self.assertEqual(camp2.comuna, dic2['comuna'])
        self.assertEqual(camp2.materiales, dic2['materiales'])
        self.assertEqual(camp2.latitud, dic2['latitud'])
        self.assertEqual(camp2.longitud, dic2['longitud'])

    def test_repr(self): # Testeamos el método __repr__ (cómo nos muestra la campana)
        self.assertEqual(str(camp1), '<AGUIRRE 1447@Cartón/Papel@CHACARITA>') # Pruebo con pocos materiales
        self.assertEqual(str(camp2), '<CASTRO 1038@Cartón/Metal/Papel/Plástico@BOEDO>') # Puebo con muchos materiales
        self.assertEqual(str(camp3), '<CASTRO 1038@@BOEDO>') # Pruebo con ningún material
        
    def test_distancia(self): # Testeamos el método que nos devuelve la distancia entre una campana y una coordenada
        self.assertEqual(camp1.distancia(0,0), 7169810.4462479055) # Probamos con el origen
        self.assertEqual(camp1.distancia(-10,-1000), 10431466.276497768) # Probamos con dos coordenadas negativas
        self.assertEqual(camp1.distancia(1000,10), 2815979.0121014197) # Probamos con dos coordenadas positivas
        self.assertEqual(camp1.distancia(-10,1000), 6599505.7648359975) # Probamos con latitud negativa y longitud positiva
        self.assertEqual(camp1.distancia(10,-1000), 12370386.1407955) # Probamos con latitud positiva y longitud negativa
        self.assertEqual(camp1.distancia(-58.4436445327415, -34.5893377789048), 0) # Probamos con las coordenadas de la campana

unittest.main()

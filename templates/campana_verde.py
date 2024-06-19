from haversine import haversine, Unit
class CampanaVerde:
    def __init__(self, direccion:str, barrio:str, comuna:int, materiales:set[str], latitud:float, longitud:float):
        '''
        Inicializa una campana verde con dirección direccion, barrio barrio, materiales materiales, 
        latitud latitud y longitud longitud.
        '''
        self.direccion:str = direccion
        self.barrio:str = barrio
        self.comuna:int = comuna
        self.materiales:set = materiales
        self.latitud:float = latitud
        self.longitud:float = longitud

    def distancia(self, lat2:float, lon2:float) -> ...:
        ''' Devuelve la distancia entre la campana verde y la ubicación dada. '''
        punto1:tuple[float, float] = (self.latitud, self.longitud)
        punto2:tuple[float, float] = (lat2, lon2)
        return haversine(punto1, punto2, unit = Unit.METERS)

    def __repr__(self) -> str:
        ''' Devuelve una representación string de la campana verde, especificando dirección, materiales y barrio. '''
        lista = list(self.materiales)
        lista.sort()
        return '<' + self.direccion + '@' + '/'.join(lista) + '@' + self.barrio + '>'

camp:CampanaVerde = CampanaVerde('AGUIRRE 1447', 'CHACARITA', 15, {'Papel', 'Cartón'}, -58.4436445327415, -34.5893377789048)
# print(camp)
print(camp.distancia(10,-1000))
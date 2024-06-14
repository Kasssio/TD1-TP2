from haversine import haversine, Unit
class CampanaVerde:
    def __init__(self, direccion:str, barrio:str, comuna:int, materiales:set[str], latitud:float, longitud:float):
        '''
        Inicializa un objeto de tipo CampanaVerde.
        Requiere: nada.
        '''
        self.direccion:str = direccion
        self.barrio:str = barrio
        self.comuna:int = comuna
        self.materiales:set = materiales
        self.latitud:float = latitud
        self.longitud:float = longitud

    def distancia(self, lat2:float, lon2:float) -> ...:
        '''
        Requiere: nada.
        Devuelve: la distancia entre la campana verde y la ubicación dada.
        '''
        punto1:tuple[float, float] = (self.latitud, self.longitud)
        punto2:tuple[float, float] = (lat2, lon2)
        return haversine(punto1, punto2, unit = Unit.METERS)

    def __repr__(self) -> str:
        ''' completar docstring '''
        #<AGUIRRE 1447@Papel/Cartón@CHACARITA>
        return '<' + self.direccion + '@' + self.materiales.split(' ') + '@' + self.barrio + '>'
        pass

camp:CampanaVerde = CampanaVerde('AGUIRRE 1447', 'CHACARITA', 15, {'Papel', 'Cartón'}, -58.4436445327415, -34.5893377789048)
print(camp)
#AGUIRRE 1447	CHACARITA	15	Papel / CartÃ³n	Los materiales deben estar limpios y secos
#POINT (-58.4436445327415 -34.5893377789048)

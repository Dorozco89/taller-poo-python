from models.obra_arte import ObraArte


class Escultura(ObraArte):

    def __init__(self, id_, titulo, valor, fecha_creacion,
                 fecha_ingreso, material, estilo):
        super().__init__(id_, titulo, valor, fecha_creacion, fecha_ingreso)
        self._material = material
        self._estilo = estilo

    def calcular_valor(self):
        return self._valor * 1.3
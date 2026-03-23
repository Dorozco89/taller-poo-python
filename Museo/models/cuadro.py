from models.obra_arte import ObraArte


class Cuadro(ObraArte):

    def __init__(self, id_, titulo, valor, fecha_creacion,
                 fecha_ingreso, tecnica, estilo):
        super().__init__(id_, titulo, valor, fecha_creacion, fecha_ingreso)
        self._tecnica = tecnica
        self._estilo = estilo

    def calcular_valor(self):
        return self._valor * 1.2
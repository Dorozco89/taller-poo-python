from models.obra_arte import ObraArte


class Objeto(ObraArte):

    def calcular_valor(self):
        return self._valor
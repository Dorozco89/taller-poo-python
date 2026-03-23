class Sala:

    def __init__(self, nombre):
        self._nombre = nombre
        self._obras = []

    def agregar_obra(self, obra):
        self._obras.append(obra)

    def listar_obras(self):
        return self._obras
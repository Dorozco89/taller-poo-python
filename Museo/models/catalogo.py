class Catalogo:

    def __init__(self):
        self._obras = []

    def agregar_obra(self, obra):
        self._obras.append(obra)

    def listar_obras(self):
        return self._obras
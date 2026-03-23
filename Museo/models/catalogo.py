class Catalogo:

    def __init__(self):
        self._obras = []

    def agregar_obra(self, obra):
        if obra is None:
            raise ValueError("No es posible agregar una obra vacía")
        self._obras.append(obra)

    def listar_obras(self):
        return self._obras

    def buscar_obra(self, id_):
        for obra in self._obras:
            if obra._id == id_:
                return obra
        return None
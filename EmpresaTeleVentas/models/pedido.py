class Pedido:
    def __init__(self, orden):
        self._orden = orden
        self._estado = "preparacion"

    def preparar_pedido(self):
        self._estado = "listo"
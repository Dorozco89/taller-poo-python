class Envio:
    def __init__(self, pedido, direccion):
        self._pedido = pedido
        self._direccion = direccion
        self._empresa = None

    def asignar_empresa(self, empresa):
        self._empresa = empresa

    def enviar(self):
        if self._empresa:
            return self._empresa.entregar_pedido()
        return "No hay empresa asignada"
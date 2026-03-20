class AgenteDeposito:
    def __init__(self, id_agente, nombre):
        self._id_agente = id_agente
        self._nombre = nombre

    def preparar_pedido(self, pedido):
        pedido.preparar_pedido()
        return "Pedido preparado por el agente"
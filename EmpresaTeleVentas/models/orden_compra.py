class OrdenCompra:
    def __init__(self, id_orden):
        self._id_orden = id_orden
        self._detalles = []
        self._estado = "pendiente"
        self._total = 0

    def agregar_producto(self, detalle):
        self._detalles.append(detalle)

    def calcular_total(self):
        self._total = sum(d.calcular_subtotal() for d in self._detalles)
        return self._total

    def confirmar_orden(self):
        self._estado = "confirmada"

    def cancelar_orden(self):
        self._estado = "cancelada"
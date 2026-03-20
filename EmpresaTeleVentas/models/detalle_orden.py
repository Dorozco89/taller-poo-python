class DetalleOrden:
    def __init__(self, producto, cantidad):
        self._producto = producto
        self._cantidad = cantidad
        self._precio_unitario = producto._precio

    def calcular_subtotal(self):
        return self._cantidad * self._precio_unitario
class Producto:
    def __init__(self, codigo, descripcion, precio, cantidad):
        self._codigo = codigo
        self._descripcion = descripcion
        self._precio = precio
        self._cantidad = cantidad

    def obtener_info(self):
        return self._descripcion
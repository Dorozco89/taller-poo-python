class Catalogo:
    def __init__(self):
        self._productos = []

    def agregar_producto(self, producto):
        self._productos.append(producto)

    def obtener_productos(self):
        return self._productos

    def buscar_producto(self, codigo):
        for producto in self._productos:
            if producto._codigo == codigo:
                return producto
        return None
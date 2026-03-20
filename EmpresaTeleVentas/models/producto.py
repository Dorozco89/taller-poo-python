class Producto:
    def __init__(self, codigo, descripcion, precio, cantidad):
        self._codigo = codigo
        self._descripcion = descripcion
        self.set_precio(precio)
        self.set_cantidad(cantidad)

    def get_codigo(self):
        return self._codigo

    def get_descripcion(self):
        return self._descripcion

    def get_precio(self):
        return self._precio

    def get_cantidad(self):
        return self._cantidad

    def set_precio(self, precio):
        if precio <= 0:
            raise ValueError("El precio debe ser mayor a 0")
        self._precio = precio

    def set_cantidad(self, cantidad):
        if cantidad < 0:
            raise ValueError("Cantidad no puede ser negativa")
        self._cantidad = cantidad
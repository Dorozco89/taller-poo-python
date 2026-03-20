class Cliente:
    def __init__(self, id_cliente, nombre, correo, direccion):
        self._id_cliente = id_cliente
        self._nombre = nombre
        self.set_correo(correo)
        self._direccion = direccion

    def get_direccion(self):
        return self._direccion

    def set_correo(self, correo):
        if "@" not in correo:
            raise ValueError("Correo inválido")
        self._correo = correo
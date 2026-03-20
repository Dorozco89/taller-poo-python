class Cliente:
    def __init__(self, id_cliente, nombre, correo, direccion):
        self._id_cliente = id_cliente
        self._nombre = nombre
        self._correo = correo
        self._direccion = direccion

    def consultar_catalogo(self, catalogo):
        return catalogo.obtener_productos()

    def crear_orden(self, orden):
        return orden

    def cancelar_orden(self, orden):
        orden.cancelar_orden()

    def presentar_queja(self, queja):
        return queja
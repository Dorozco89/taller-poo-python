class GerenteRelaciones:
    def __init__(self, id_gerente, nombre, correo):
        self._id_gerente = id_gerente
        self._nombre = nombre
        self._correo = correo

    def gestionar_queja(self, queja):
        return f"Queja gestionada por {self._nombre}"
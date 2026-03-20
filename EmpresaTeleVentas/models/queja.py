class Queja:
    def __init__(self, descripcion):
        self._descripcion = descripcion
        self._estado = "nueva"

    def registrar_queja(self):
        self._estado = "registrada"

    def notificar_gerente(self, gerente):
        return gerente.gestionar_queja(self)
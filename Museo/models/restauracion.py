class Restauracion:

    def __init__(self, tipo, fecha_inicio):
        if not tipo:
            raise ValueError("Tipo de restauración obligatorio")

        self._tipo = tipo
        self._fecha_inicio = fecha_inicio
        self._fecha_fin = None

    def finalizar(self, fecha_fin):
        self._fecha_fin = fecha_fin
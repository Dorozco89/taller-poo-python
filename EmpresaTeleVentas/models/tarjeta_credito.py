from models.pago import Pago


class TarjetaCredito(Pago):
    def __init__(self, monto, numero, titular):
        super().__init__(monto)
        self._numero = numero
        self._titular = titular

    def procesar_pago(self):
        self._estado = "aprobado"
        return True
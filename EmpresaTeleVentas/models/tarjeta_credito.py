from models.pago import Pago


class TarjetaCredito(Pago):
    def __init__(self, monto, numero, titular, fecha, cvv):
        super().__init__(monto)
        self._numero = numero
        self._titular = titular
        self._fecha = fecha
        self._cvv = cvv

    def procesar_pago(self):
        if len(str(self._numero)) < 6:
            return False
        self._estado = "aprobado"
        return True
from abc import ABC, abstractmethod


class Pago(ABC):
    def __init__(self, monto):
        self._monto = monto
        self._estado = "pendiente"

    @abstractmethod
    def procesar_pago(self):
        pass
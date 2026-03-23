from abc import ABC, abstractmethod


class ObraArte(ABC):

    def __init__(self, id_, titulo, valor, fecha_creacion, fecha_ingreso):
        self._id = id_
        self._titulo = titulo
        self._valor = valor
        self._fecha_creacion = fecha_creacion
        self._fecha_ingreso = fecha_ingreso
        self._estado = "expuesta"

    def cambiar_estado(self, estado):
        self._estado = estado

    @abstractmethod
    def calcular_valor(self):
        pass
from abc import ABC, abstractmethod


class ObraArte(ABC):

    def __init__(self, id_, titulo, valor, fecha_creacion, fecha_ingreso):
        if id_ <= 0:
            raise ValueError("ID inválido")

        if valor <= 0:
            raise ValueError("El valor debe ser mayor a 0")

        self._id = id_
        self._titulo = titulo
        self._valor = valor
        self._fecha_creacion = fecha_creacion
        self._fecha_ingreso = fecha_ingreso
        self._estado = "expuesta"
        self._restauraciones = []

    def cambiar_estado(self, estado):
        if estado not in ["expuesta", "restauracion"]:
            raise ValueError("Estado inválido")
        self._estado = estado

    def agregar_restauracion(self, restauracion):
        self._restauraciones.append(restauracion)

    def get_titulo(self):
        return self._titulo

    def get_valor(self):
        return self._valor

    @abstractmethod
    def calcular_valor(self):
        pass
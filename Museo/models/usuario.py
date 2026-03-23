from abc import ABC


class Usuario(ABC):

    def __init__(self, id_, nombre, correo, password):
        self._id = id_
        self._nombre = nombre
        self._correo = correo
        self._password = password
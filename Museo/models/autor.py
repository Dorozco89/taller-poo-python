class Autor:

    def __init__(self, nombre, nacionalidad):
        self._nombre = nombre
        self._nacionalidad = nacionalidad

    def get_nombre(self):
        return self._nombre
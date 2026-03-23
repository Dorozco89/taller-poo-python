from models.usuario import Usuario


class EncargadoCatalogo(Usuario):

    def registrar_obra(self, catalogo, obra):
        catalogo.agregar_obra(obra)
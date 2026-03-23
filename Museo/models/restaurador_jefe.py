from models.usuario import Usuario


class RestauradorJefe(Usuario):

    def consultar_restauraciones(self, obra):
        return obra._restauraciones
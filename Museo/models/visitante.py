from models.usuario import Usuario


class Visitante(Usuario):

    def consultar_obras(self, sala):
        return sala.listar_obras()
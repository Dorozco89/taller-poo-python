from models.usuario import Usuario


class Director(Usuario):

    def calcular_valor_total(self, catalogo):
        total = 0
        for obra in catalogo.listar_obras():
            total += obra.calcular_valor()
        return total
class Autenticacion:

    def login(self, usuario, password):
        if not usuario or not password:
            raise ValueError("Datos incompletos")

        return usuario._password == password
from models.cuadro import Cuadro
from models.catalogo import Catalogo
from models.director import Director


def main():
    catalogo = Catalogo()

    cuadro = Cuadro(1, "Mona Lisa", 1000, "1503", "2020",
                    "Óleo", "Renacimiento")

    catalogo.agregar_obra(cuadro)

    director = Director(1, "Alberto", "correo@mail.com", "123")

    total = director.calcular_valor_total(catalogo)

    print("Valor total del museo:", total)


if __name__ == "__main__":
    main()
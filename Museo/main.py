from models.cuadro import Cuadro
from models.escultura import Escultura
from models.objeto import Objeto
from models.catalogo import Catalogo
from models.autor import Autor
from models.periodo import Periodo
from models.restauracion import Restauracion
from models.museo import Museo
from models.cesion import Cesion
from models.sala import Sala
from models.director import Director
from models.restaurador_jefe import RestauradorJefe
from models.encargado_catalogo import EncargadoCatalogo
from models.visitante import Visitante
from services.autenticacion import Autenticacion


def main():
    print("=== SISTEMA MUSEO ===\n")

    # DATOS INICIALES
    autor = Autor("Leonardo da Vinci", "Italia")
    periodo = Periodo("Renacimiento", "Siglo XV")
    

    cuadro = Cuadro(1, "Mona Lisa", 1000, "1503", "2020",
                    "Óleo", "Renacimiento")

    escultura = Escultura(2, "David", 2000, "1504", "2021",
                          "Mármol", "Renacimiento")

    objeto = Objeto(3, "Vasija Antigua", 500, "1200", "2019")


    catalogo = Catalogo()
    encargado = EncargadoCatalogo(1, "Santiago",
                                 "correo@mail.com", "123")

    encargado.registrar_obra(catalogo, cuadro)
    encargado.registrar_obra(catalogo, escultura)
    encargado.registrar_obra(catalogo, objeto)


    sala = Sala("Sala Principal")
    sala.agregar_obra(cuadro)
    sala.agregar_obra(escultura)

    visitante = Visitante(3, "Pedro", "visit@mail.com", "123")
    restaurador = RestauradorJefe(2, "Maria",
                                 "maria@mail.com", "123")

    director = Director(4, "Alberto",
                        "alb@mail.com", "123")

    auth = Autenticacion()

    while True:
        print("\n===== MENÚ MUSEO =====")
        print("1. Ver catálogo")
        print("2. Restaurar obra")
        print("3. Ver obras en sala")
        print("4. Ceder obra")
        print("5. Calcular valor total")
        print("6. Login")
        print("7. Salir")

        opcion = input("Seleccione: ")

        # 1. VER CATÁLOGO
        if opcion == "1":
            print("\nObras en catálogo:")
            for obra in catalogo.listar_obras():
                print(f"- {obra.get_titulo()} (${obra.get_valor()})")

        # 2. RESTAURAR OBRA
        elif opcion == "2":
            restauracion = Restauracion("Limpieza", "2024-01-01")
            cuadro.agregar_restauracion(restauracion)

            print("Restauración aplicada a:",
                  cuadro.get_titulo())

        # 3. VER SALA
        elif opcion == "3":
            print("\nObras en sala:")
            for obra in visitante.consultar_obras(sala):
                print("-", obra.get_titulo())

        # 4. CESIÓN
        elif opcion == "4":
            museo_externo = Museo("Museo Louvre", "Francia")

            cesion = Cesion("2025-01-01",
                            "2025-12-31",
                            10000,
                            museo_externo)

            print("Obra cedida a:", museo_externo._nombre)

        # 5. VALOR TOTAL
        elif opcion == "5":
            total = director.calcular_valor_total(catalogo)
            print("Valor total del museo:", total)

        # 6. LOGIN
        elif opcion == "6":
            correo = input("Correo: ")
            password = input("Password: ")

            print("Login correcto:",
                  auth.login(director, password))

        # 7. SALIR
        elif opcion == "7":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()
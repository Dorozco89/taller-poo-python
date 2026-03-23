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

    # -------------------------
    # 1. Crear autor y periodo
    # -------------------------
    autor = Autor("Leonardo da Vinci", "Italia")
    periodo = Periodo("Renacimiento", "Siglo XV")

    # -------------------------
    # 2. Crear obras
    # -------------------------
    cuadro = Cuadro(1, "Mona Lisa", 1000, "1503", "2020",
                    "Óleo", "Renacimiento")

    escultura = Escultura(2, "David", 2000, "1504", "2021",
                          "Mármol", "Renacimiento")

    objeto = Objeto(3, "Vasija Antigua", 500, "1200", "2019")

    # -------------------------
    # 3. Catálogo
    # -------------------------
    catalogo = Catalogo()
    encargado = EncargadoCatalogo(1, "Santiago", "correo@mail.com", "123")

    encargado.registrar_obra(catalogo, cuadro)
    encargado.registrar_obra(catalogo, escultura)
    encargado.registrar_obra(catalogo, objeto)

    print("Obras en catálogo:")
    for obra in catalogo.listar_obras():
        print(f"- {obra.get_titulo()} (${obra.get_valor()})")

    # -------------------------
    # 4. Restauración
    # -------------------------
    restaurador = RestauradorJefe(2, "Maria", "maria@mail.com", "123")

    restauracion = Restauracion("Limpieza", "2024-01-01")
    cuadro.agregar_restauracion(restauracion)

    print("\nRestauración agregada a:", cuadro.get_titulo())

    # -------------------------
    # 5. Sala y visitante
    # -------------------------
    sala = Sala("Sala Principal")
    sala.agregar_obra(cuadro)
    sala.agregar_obra(escultura)

    visitante = Visitante(3, "Pedro", "visit@mail.com", "123")

    print("\nObras en sala:")
    for obra in visitante.consultar_obras(sala):
        print("-", obra.get_titulo())

    # -------------------------
    # 6. Cesión
    # -------------------------
    museo_externo = Museo("Museo Louvre", "Francia")

    cesion = Cesion("2025-01-01", "2025-12-31", 10000, museo_externo)

    print("\nObra cedida a:", museo_externo._nombre)

    # -------------------------
    # 7. Director consulta el valor total
    # -------------------------
    director = Director(4, "Alberto", "alb@mail.com", "123")

    total = director.calcular_valor_total(catalogo)

    print("\nValor total del museo:", total)

    # -------------------------
    # 8. Autenticación
    # -------------------------
    auth = Autenticacion()

    print("\nLogin correcto:",
          auth.login(director, "123"))

    print("\n=== FIN DEL SISTEMA ===")


if __name__ == "__main__":
    main()
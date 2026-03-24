from models.cliente import Cliente
from models.producto import Producto
from models.catalogo import Catalogo
from models.detalle_orden import DetalleOrden
from models.orden_compra import OrdenCompra
from models.tarjeta_credito import TarjetaCredito
from models.pedido import Pedido
from models.envio import Envio
from models.empresa_transporte import EmpresaTransporte
from models.queja import Queja
from models.agente_deposito import AgenteDeposito
from models.gerente_relaciones import GerenteRelaciones


def main():
    print("=== SISTEMA EMPRESA TELEVENTAS ===\n")
    

    cliente = Cliente(1, "David", "david01@email.com", "Calle 123")


    producto1 = Producto("001", "Laptop", 2000, 10)
    producto2 = Producto("002", "Mouse", 50, 100)

    catalogo = Catalogo()
    catalogo.agregar_producto(producto1)
    catalogo.agregar_producto(producto2)

    gerente = GerenteRelaciones(1, "Paula", "paula@email.com")
    agente = AgenteDeposito(1, "Carlos")

    orden = None
    pedido = None

    while True:
        print("\n===== MENÚ TELEVENTAS =====")
        print("1. Ver catálogo")
        print("2. Crear orden de compra")
        print("3. Procesar pago")
        print("4. Preparar y enviar pedido")
        print("5. Registrar queja")
        print("6. Salir")

        opcion = input("Seleccione: ")

        # 1. VER CATÁLOGO
        if opcion == "1":
            print("\nProductos disponibles:")
            for p in catalogo.obtener_productos():
                print(f"- {p.get_descripcion()} (${p.get_precio()})")

        # 2. CREAR ORDEN
        elif opcion == "2":
            orden = OrdenCompra(1)

            detalle1 = DetalleOrden(producto1, 1)
            detalle2 = DetalleOrden(producto2, 2)

            orden.agregar_producto(detalle1)
            orden.agregar_producto(detalle2)

            total = orden.calcular_total()
            print(f"\nTotal de la orden: ${total}")

            orden.confirmar_orden()

        # 3. PAGO
        elif opcion == "3":
            if orden is None:
                print("Primero crea una orden")
                continue

            total = orden.calcular_total()

            pago = TarjetaCredito(total, "123456789",
                                  "David", "12/28", 123)

            if pago.procesar_pago():
                print("Pago aprobado")
            else:
                print("Pago rechazado")

        # 4. PEDIDO + ENVÍO
        elif opcion == "4":
            if orden is None:
                print("Primero crea una orden")
                continue

            pedido = Pedido(orden)

            print(agente.preparar_pedido(pedido))

            envio = Envio(pedido, cliente.get_direccion())
            empresa = EmpresaTransporte("DHL")

            envio.asignar_empresa(empresa)

            print(envio.enviar())

        # 5. QUEJA
        elif opcion == "5":
            descripcion = input("Describe la queja: ")

            queja = Queja(descripcion)
            queja.registrar_queja()

            print(queja.notificar_gerente(gerente))

        # 6. SALIR
        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida")


if __name__ == "__main__":
    main()
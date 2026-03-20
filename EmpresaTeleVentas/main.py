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

    # -------------------------
    # 1. Crear cliente
    # -------------------------
    cliente = Cliente(1, "David", "david01@email.com", "Calle 123")

    # -------------------------
    # 2. Crear productos y catálogo
    # -------------------------
    producto1 = Producto("001", "Laptop", 2000, 10)
    producto2 = Producto("002", "Mouse", 50, 100)

    catalogo = Catalogo()
    catalogo.agregar_producto(producto1)
    catalogo.agregar_producto(producto2)

    print("Productos disponibles:")
    for p in catalogo.obtener_productos():
        print(f"- {p.get_descripcion()} (${p.get_precio()})")

    # -------------------------
    # 3. Crear orden de compra
    # -------------------------
    orden = OrdenCompra(1)

    detalle1 = DetalleOrden(producto1, 1)
    detalle2 = DetalleOrden(producto2, 2)

    orden.agregar_producto(detalle1)
    orden.agregar_producto(detalle2)

    total = orden.calcular_total()
    print(f"\nTotal de la orden: ${total}")

    orden.confirmar_orden()

    # -------------------------
    # 4. Procesar pago
    # -------------------------
    pago = TarjetaCredito(total, "123456789", "David", "12/28", 123)

    if pago.procesar_pago():
        print("Pago aprobado")
    else:
        print("Pago rechazado")

    # -------------------------
    # 5. Crear pedido
    # -------------------------
    pedido = Pedido(orden)

    agente = AgenteDeposito(1, "Carlos")
    print(agente.preparar_pedido(pedido))

    # -------------------------
    # 6. Envío
    # -------------------------
    envio = Envio(pedido, cliente.get_direccion())

    empresa = EmpresaTransporte("DHL")
    envio.asignar_empresa(empresa)

    print(envio.enviar())

    # -------------------------
    # 7. Queja
    # -------------------------
    queja = Queja("Demora en la entrega")
    queja.registrar_queja()

    gerente = GerenteRelaciones(1, "Ana", "ana@email.com")
    print(queja.notificar_gerente(gerente))

    print("\n=== FIN DEL PROCESO ===")


if __name__ == "__main__":
    main()
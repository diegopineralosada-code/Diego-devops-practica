from services.Tienda_service import TiendaService
from models.Producto import ProductoElectronico, ProductoRopa, Producto


def main():
    """
    Script principal de demostración del sistema de tienda.
        1. Se crean usuarios (clientes y administrador).
        2. Se registran productos en la tienda.
        3. Los clientes realizan pedidos con distintos productos.
        4. Se muestran:
            - Usuarios registrados.
            - Inventario inicial.
            - Pedidos creados.
            - Histórico de pedidos por cliente.
            - Stock actualizado tras los pedidos.
    """
    tienda = TiendaService()

    c1 = tienda.registrar_usuario("cliente", nombre="Fernado Pemán", email="fernando@gmail.com", direccion_postal="Av Pablo Picasso 123")
    c2 = tienda.registrar_usuario("cliente", nombre="Mario Tuset", email="mario@gmail.com", direccion_postal="Plaza Casares Quiroga 7")
    c3 = tienda.registrar_usuario("cliente", nombre="Nicolás Cerqueiro", email="nicolas@gmail.com", direccion_postal="Av Caballero 5")
    admin = tienda.registrar_usuario("administrador", nombre="Diego Piñera", email="admin@gmail.com")

    print("Usuarios registrados:")
    for u in (c1, c2, c3, admin):
        print(u)
    print("-" * 60)

    p1 = ProductoElectronico(nombre="Portátil logo Lorna Shore", precio=399.99, stock=10, garantia_meses=24)
    p2 = ProductoElectronico(nombre="Auriculares logo Wind Rose", precio=59.90, stock=25, garantia_meses=12)
    p3 = ProductoRopa(nombre="Camiseta Sabaton", precio=12.50, stock=50, talla="M", color="Gris")
    p4 = ProductoRopa(nombre="Chaqueta Powerwolf", precio=89.99, stock=5, talla="L", color="Negro")
    p5 = Producto(nombre="Libro: La historia del Metal", precio=29.95, stock=20)

    for p in (p1, p2, p3, p4, p5):
        tienda.agregar_producto(p)

    print("Inventario inicial:")
    for prod in tienda.listar_productos():
        print(prod)
    print("-" * 60)

    pedido1 = tienda.realizar_pedido(c1.id, {p1.id: 1, p2.id: 2})
    print("Pedido 1 creado:")
    print(pedido1)
    print("-" * 60)

    pedido2 = tienda.realizar_pedido(c2.id, {p3.id: 3, p5.id: 1})
    print("Pedido 2 creado:")
    print(pedido2)
    print("-" * 60)

    pedido3 = tienda.realizar_pedido(c3.id, {p4.id: 1})
    print("Pedido 3 creado:")
    print(pedido3)
    print("-" * 60)

    print(f"Histórico de pedidos de {c1.nombre}:")
    pedidos_ana = tienda.listar_pedidos_usuario(c1.id)
    for p in pedidos_ana:
        print(p)
        print("---")
    print("-" * 60)

    print("Stock actualizado tras pedidos:")
    for prod in tienda.listar_productos():
        print(prod)
    print("-" * 60)


if __name__ == "__main__":
    main()

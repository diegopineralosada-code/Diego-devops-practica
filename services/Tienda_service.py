from __future__ import annotations
from typing import Dict, List, Tuple
from models.Producto import Producto, ProductoElectronico, ProductoRopa
from models.Usuario import Usuario, Cliente, Administrador
from models.Pedido import Pedido
from datetime import datetime


class TiendaService:
    """
    Servicio principal de la tienda. Gestiona usuarios, productos y pedidos.
        _productos: productos disponibles.
        _usuarios: usuarios registrados.
        _pedidos: lista de pedidos realizados.
    """
    def __init__(self) -> None:
        """Inicializa la tienda con colecciones vacías de usuarios, productos y pedidos."""
        self._productos: Dict[str, Producto] = {}
        self._usuarios: Dict[str, Usuario] = {}
        self._pedidos: List[Pedido] = []

    def registrar_usuario(self, tipo: str, nombre: str, email: str, **kwargs) -> Usuario:
        """
        Registra un nuevo usuario en la tienda.
            tipo: tipo de usuario.
            nombre: nombre del usuario.
            email: correo electrónico.
            **kwargs: argumentos adicionales.

        Devuelve:
            Usuario: el usuario creado.

        Raises:
            ValueError: si el tipo de usuario no es válido.
        """
        tipo_lower = tipo.strip().lower()
        if tipo_lower == "cliente":
            direccion = kwargs.get("direccion_postal", "")
            usuario = Cliente(nombre=nombre, email=email, direccion_postal=direccion)
        elif tipo_lower == "administrador" or tipo_lower == "admin":
            usuario = Administrador(nombre=nombre, email=email)
        else:
            raise ValueError("Tipo de usuario desconocido. Use 'cliente' o 'administrador'.")
        self._usuarios[usuario.id] = usuario
        return usuario

    def obtener_usuario(self, usuario_id: str) -> Usuario:
        """
        Obtiene un usuario por su id.
            usuario_id: identificador del usuario.

        Devuelve:
            Usuario: el usuario encontrado.

        Raises:
            KeyError: si el usuario no existe.
        """
        usuario = self._usuarios.get(usuario_id)
        if usuario is None:
            raise KeyError(f"Usuario con id {usuario_id} no encontrado.")
        return usuario

    def agregar_producto(self, producto: Producto) -> Producto:
        """
        Agrega un producto al inventario.
            producto: Producto a agregar.

        Devuelve:
            Producto: el producto agregado.
        """
        self._productos[producto.id] = producto
        return producto

    def eliminar_producto(self, producto_id: str) -> None:
        """
        Elimina un producto del inventario.
            producto_id: identificador del producto a eliminar.

        Raises:
            KeyError: si el producto no existe.
        """
        if producto_id not in self._productos:
            raise KeyError(f"Producto con id {producto_id} no encontrado.")
        del self._productos[producto_id]

    def listar_productos(self) -> List[Producto]:
        """
        Lista todos los productos disponibles.

        Devuelve:
            List[Producto]: lista de productos en el inventario.
        """
        return list(self._productos.values())

    def obtener_producto(self, producto_id: str) -> Producto:
        """
        Obtiene un producto por su id.
            producto_id: identificador del producto.

        Devuelve:
            Producto: el producto encontrado.

        Raises:
            KeyError: si el producto no existe.
        """
        producto = self._productos.get(producto_id)
        if producto is None:
            raise KeyError(f"Producto con id {producto_id} no encontrado.")
        return producto

    def realizar_pedido(self, usuario_id: str, items_por_id: Dict[str, int]) -> Pedido:
        """
        Permite a un cliente realizar un pedido.
            usuario_id: identificador del cliente.
            items_por_id: diccionario {id_producto: cantidad}.

        Devuelve:
            Pedido: el pedido generado.

        Raises:
            KeyError: si el usuario o algún producto no existe.
            PermissionError: si el usuario no es un cliente.
            ValueError: si la cantidad es inválida o no hay suficiente stock.
        """
        usuario = self._usuarios.get(usuario_id)
        if usuario is None:
            raise KeyError(f"Usuario con id {usuario_id} no encontrado.")
        if not isinstance(usuario, Cliente):
            raise PermissionError("Sólo clientes pueden realizar pedidos.")

        productos_y_cantidades: List[Tuple[Producto, int]] = []
        for pid, cantidad in items_por_id.items():
            if cantidad <= 0:
                raise ValueError("La cantidad debe ser mayor que 0.")
            producto = self._productos.get(pid)
            if producto is None:
                raise KeyError(f"Producto con id {pid} no encontrado.")
            if not producto.hay_stock(cantidad):
                raise ValueError(f"Stock insuficiente para el producto '{producto.nombre}' (id={pid}).")
            productos_y_cantidades.append((producto, cantidad))

        # Actualizar stock
        for producto, cantidad in productos_y_cantidades:
            producto.actualizar_stock(-cantidad)

        pedido = Pedido(cliente_id=usuario_id, items=productos_y_cantidades, fecha=datetime.now())
        self._pedidos.append(pedido)
        return pedido

    def listar_pedidos_usuario(self, usuario_id: str) -> List[Pedido]:
        """
        Lista los pedidos de un cliente ordenados por fecha.
            usuario_id: identificador del cliente.

        Devuelve:
            List[Pedido]: lista de pedidos realizados por el cliente.

        Raises:
            KeyError: si el usuario no existe.
        """
        if usuario_id not in self._usuarios:
            raise KeyError(f"Usuario con id {usuario_id} no encontrado.")
        pedidos_usuario = [p for p in self._pedidos if p.cliente_id == usuario_id]
        pedidos_usuario.sort(key=lambda p: p.fecha)
        return pedidos_usuario

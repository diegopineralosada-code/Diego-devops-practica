from __future__ import annotations
from typing import Any
import uuid


class Producto:
    """
    Representa un producto genérico dentro del sistema.
        nombre: nombre del producto.
        precio: precio del producto.
        stock: cantidad disponible en inventario.
        id: identificador único del producto.
    """
    def __init__(self, nombre: str, precio: float, stock: int, id: str = None):
        """
        Inicializa un nuevo producto.
            nombre (str): nombre del producto.
            precio (float): precio del producto.
            stock (int): cantidad inicial en inventario.
            id (str, opcional): identificador único del producto. 
        """
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.id = id if id is not None else str(uuid.uuid4())

    def hay_stock(self, cantidad: int) -> bool:
        """
        Verifica si existe suficiente stock disponible.
            cantidad (int): Cantidad solicitada.
        
        Devuelve:
            bool: True si hay suficiente stock, False en caso contrario.
        """
        return cantidad <= self.stock

    def actualizar_stock(self, cantidad: int) -> None:
        """
        Modifica el stock del producto.
            cantidad (int): cantidad a modificar.
                - Positivo: incrementa el stock.
                - Negativo: reduce el stock.

        Raises:
            ValueError: Si el nuevo stock es negativo.
        """
        nuevo = self.stock + cantidad
        if nuevo < 0:
            raise ValueError(f"Stock insuficiente para {self.nombre} (id={self.id}).")
        self.stock = nuevo

    def __str__(self) -> str:
        """
        Devuelve una representación legible del producto.

        Devuelve:
            str: cadena con la información básica del producto.
        """
        return f"[{self.id}] {self.nombre} - Precio: {self.precio:.2f} € - Stock: {self.stock}"


class ProductoElectronico(Producto):
    """
    Representa un producto de tipo electrónico.
        garantia_meses: Duración de la garantía en meses.
    """
    def __init__(self, nombre: str, precio: float, stock: int, garantia_meses: int = 0, id: str = None):
        """
        Inicializa un nuevo producto electrónico.
            nombre: nombre del producto.
            precio: precio unitario.
            stock: cantidad en inventario.
            garantia_meses: garantía en meses. Por defecto es 0.
            id: identificador único.
        """
        super().__init__(nombre, precio, stock, id)
        self.garantia_meses = garantia_meses

    def __str__(self) -> str:
        """
        Devuelve una representación legible del producto electrónico, incluyendo la garantía.

        Devuelve:
            str: cadena con la información del producto.
        """
        base = super().__str__()
        return f"{base} - Garantía: {self.garantia_meses} meses"


class ProductoRopa(Producto):
    """
    Representa un producto de tipo ropa.
        talla (str): Talla de la prenda.
        color (str): Color de la prenda.
    """
    def __init__(self, nombre: str, precio: float, stock: int, talla: str = "", color: str = "", id: str = None):
        """
        Inicializa un nuevo producto de ropa.
            nombre: nombre del producto.
            precio: precio unitario.
            stock: cantidad en inventario.
            talla: talla de la prenda.
            color: color de la prenda.
            id: identificador único.
        """
        super().__init__(nombre, precio, stock, id)
        self.talla = talla
        self.color = color

    def __str__(self) -> str:
        """
        Devuelve una representación legible del producto de ropa, incluyendo talla y color si están definidos.

        Devuelve:
            str: cadena con la información del producto.
        """
        base = super().__str__()
        extras = []
        if self.talla:
            extras.append(f"Talla: {self.talla}")
        if self.color:
            extras.append(f"Color: {self.color}")
        extras_text = " - ".join(extras) if extras else ""
        return f"{base} - {extras_text}"
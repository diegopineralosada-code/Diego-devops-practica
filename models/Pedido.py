from __future__ import annotations
from datetime import datetime
from typing import List, Tuple
import uuid


class Pedido: 
    """
    Representa un pedido realizado por un cliente.
        cliente_id: identificador único del cliente.
        items: lista de productos y sus cantidades (se espera que producto tenga id, nombre y precio).
        fecha: fecha y hora del pedido
        id: identificador único del pedido.
    """
    def __init__(self, cliente_id: str, items: List[Tuple[object, int]] = None, fecha: datetime = None, id: str = None):
        """
        Inicializa un nuevo pedido.
        cliente_id: identificador del cliente.
        items: lista de productos con sus cantidades.
        fecha: fecha del pedido.
        id: identificador del pedido.
        """
        self.cliente_id = cliente_id
        self.items = items if items is not None else []
        self.fecha = fecha if fecha is not None else datetime.now()
        self.id = id if id is not None else str(uuid.uuid4())

    def calcular_total(self) -> float:
        """
        Calcula el precio total del pedido sumando el precio de cada producto multiplicado por su cantidad.

        Devuelve: 
            float: el importe total del pedido.
        """
        total = 0.0
        for producto, cantidad in self.items:
            total += float(producto.precio) * cantidad
        return total

    def __str__(self) -> str:
        """
        Devuelve una representación en forma de cadena del pedido, incluyendo
        información del cliente, los productos, cantidades y el total.

        Devuelve:
            str: representación legible del pedido.
        """
        lines = [f"Pedido [{self.id}] - Fecha: {self.fecha.isoformat()}"]
        lines.append(f"Cliente id: {self.cliente_id}")
        lines.append("Items:")
        for producto, cantidad in self.items:
            lines.append(f"  - {producto.nombre} (id={producto.id}) x {cantidad} -> {producto.precio:.2f} €/ud")
        lines.append(f"Total: {self.calcular_total():.2f} €")
        return "\n".join(lines)
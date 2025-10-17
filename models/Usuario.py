from __future__ import annotations
import uuid


class Usuario:
    """
    Representa un usuario genérico del sistema.
        nombre: nombre del usuario.
        email: correo electrónico del usuario.
        id: identificador único del usuario.
    """
    def __init__(self, nombre: str, email: str, id: str = None):
        """
        Inicializa un nuevo usuario.
            nombre: nombre del usuario.
            email: dirección de correo electrónico.
            id: identificador único.
        """
        self.nombre = nombre
        self.email = email
        self.id = id if id is not None else str(uuid.uuid4())

    def is_admin(self) -> bool:
        """
        Verifica si el usuario es administrador.

        Devuelve:
            bool: False por defecto, sobrescrito en la subclase Administrador.
        """
        return False

    def __str__(self) -> str:
        """
        Devuelve una representación legible del usuario, incluyendo su rol.

        Devuelve:
            str: cadena con la información del usuario.
        """
        rol = "Administrador" if self.is_admin() else "Cliente/Usuario"
        return f"[{self.id}] {self.nombre} <{self.email}> - {rol}"


class Cliente(Usuario):
    """
    Representa un cliente registrado en el sistema.
        direccion_postal: dirección física del cliente.
    """
    def __init__(self, nombre: str, email: str, direccion_postal: str = "", id: str = None):
        """
        Inicializa un nuevo cliente.
            nombre: nombre del cliente.
            email: correo electrónico del cliente.
            direccion_postal: dirección física del cliente.
            id: identificador único. 
        """
        super().__init__(nombre, email, id)
        self.direccion_postal = direccion_postal

    def __str__(self) -> str:
        """
        Devuelve una representación legible del cliente, incluyendo la dirección postal.

        Devuelve:
            str: Cadena con la información del cliente.
        """
        base = super().__str__()
        return f"{base} - Dirección: {self.direccion_postal}"


class Administrador(Usuario):
    """
    Representa un usuario con rol de administrador.
    """
    def __init__(self, nombre: str, email: str, id: str = None):
        """
        Inicializa un nuevo administrador.
            nombre: nombre del administrador.
            email: correo electrónico del administrador.
            id: identificador único.
        """
        super().__init__(nombre, email, id)

    def is_admin(self) -> bool:
        """
        Sobrescribe el método base para indicar que este usuario es administrador.

        Devuelve:
            bool: True siempre.
        """
        return True

    def __str__(self) -> str:
        """
        Devuelve una representación legible del administrador.

        Devuelve:
            str: cadena con la información del administrador.
        """
        return f"[{self.id}] {self.nombre} <{self.email}> - Administrador"
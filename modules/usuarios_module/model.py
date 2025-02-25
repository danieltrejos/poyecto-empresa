from database.db import db
from typing import List, Optional


class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id_usuario: int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    nombre: str = db.Column(db.String(50), nullable=False)
    apellido: str = db.Column(db.String(50), nullable=False)
    tipo_documento: str = db.Column(db.String(20), nullable=False)
    num_documento: str = db.Column(db.String(20), nullable=False, unique=True)
    telefono: Optional[str] = db.Column(db.String(20), nullable=True)
    direccion: Optional[str]  = db.Column(db.String(255), nullable=True)
    email: Optional[str]  = db.Column(db.String(100), nullable=False, unique=True)
    username: str = db.Column(db.String(50), nullable=False, unique=True)
    password: str = db.Column(db.String(255), nullable=False)

    rol: str = db.Column(db.Enum('admin', 'cliente', name='rol_enum'), nullable=False)
    estado: Optional[str] = db.Column(db.Enum('ACTIVO', 'NO_ACTIVO', name='estado_usuario_enum'),nullable=True, default='ACTIVO')
    privilegio: Optional[str] = db.Column(db.String(50), nullable=True)

    #! Descomentar
    # Relación uno a uno con PerfilCliente
    # perfil_cliente = db.relationship('PerfilCliente', back_populates='usuario', uselist=False, cascade="all, delete")
    
    # Relación uno a muchos con Transaccion (usuario que registra transacciones)
    # transacciones = db.relationship('Transaccion', back_populates='usuario', cascade="all, delete")

"""  def to_dict(self) -> dict:
        return {
            "id_usuario": self.id_usuario,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "tipo_documento": self.tipo_documento,
            "num_documento": self.num_documento,
            "telefono": self.telefono,
            "direccion": self.direccion,
            "email": self.email,
            "username": self.username,
            "rol": self.rol,
            "estado": self.estado,
            "privilegio": self.privilegio
        }
"""
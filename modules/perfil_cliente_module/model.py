from database.db import db

class PerfilCliente(db.Model):
    __tablename__ = 'perfil_cliente'
    id_perfil_cliente = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    entidad_bancaria = db.Column(db.String(100), nullable=True)
    tipo_cuenta = db.Column(db.Enum('Ahorros', 'Corriente', name='tipo_cuenta_enum'), nullable=False)
    numero_cuenta = db.Column(db.String(50), nullable=False, unique=True)
    num_documento = db.Column(db.String(20), nullable=False, unique=True)

    # Clave foranea con usuario relacion 1 a 1
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario', ondelete='CASCADE'), nullable=False, unique=True)
    
    # Relación con Usuario (uno a uno)
    usuario = db.relationship('Usuario', back_populates='perfil_cliente')
    
    # Relación uno a muchos: Un perfil puede tener varios préstamos
    prestamos = db.relationship('Prestamo', back_populates='cliente', cascade="all, delete")

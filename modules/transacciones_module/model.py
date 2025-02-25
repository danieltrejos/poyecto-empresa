from database.db import db
from sqlalchemy import func

class Transaccion(db.Model):
    __tablename__ = 'transacciones'
    id_transaccion = db.Column(db.Integer, primary_key=True, autoincrement=True)
    monto = db.Column(db.Numeric(12, 2), nullable=False)
    fecha_transaccion = db.Column(db.DateTime, nullable=False, server_default=func.current_timestamp())
    tipo_transaccion = db.Column(db.Enum('INCREMENTO', 'ABONO_CAPITAL', 'INTERES', 'ABONO_INTERESES', name='tipo_transaccion_enum'), nullable=False)
    
    # Relación con Prestamo y Usuario claves foraneas
    prestamo_id = db.Column(db.Integer, db.ForeignKey('prestamos.id_prestamo', ondelete='CASCADE'), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id_usuario', ondelete='CASCADE'), nullable=False)

    # Relación con Prestamo y Usuario
    prestamo = db.relationship('Prestamo', back_populates='transacciones')
    usuario = db.relationship('Usuario', back_populates='transacciones')
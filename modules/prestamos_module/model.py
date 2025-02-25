from database.db import db

class Prestamo(db.Model):
    __tablename__ = 'prestamos'
    
    id_prestamo = db.Column(db.Integer, primary_key=True, autoincrement=True)
    prestamo_codigo = db.Column(db.String(20), nullable=False, unique=True)
    tasa_interes = db.Column(db.Numeric(5, 2), nullable=False)
    fecha_inicio = db.Column(db.Date, nullable=False)
    fecha_final = db.Column(db.Date, nullable=False)
    plazo_meses = db.Column(db.Integer, nullable=False)
    estado = db.Column(db.Enum('ACTIVO', 'PAGADO', 'VENCIDO', name='estado_prestamo_enum'), nullable=False)
    monto_prestamo = db.Column(db.Numeric(12, 2), nullable=False)
    monto_intereses = db.Column(db.Numeric(12, 2), nullable=False)
    total = db.Column(db.Numeric(12, 2), nullable=False)
    pagado = db.Column(db.Numeric(12, 2), nullable=True, default=0)
    saldo_pendiente = db.Column(db.Numeric(12, 2), nullable=False)
    observacion = db.Column(db.Text, nullable=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('perfil_cliente.id_perfil_cliente', ondelete='CASCADE'),  nullable=False)

    # Relación con PerfilCliente
    cliente = db.relationship('PerfilCliente', back_populates='prestamos')
    # Relación uno a muchos: Un préstamo puede tener varias transacciones
    transacciones = db.relationship('Transaccion', back_populates='prestamo',   cascade="all, delete")
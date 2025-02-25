from run import create_app
from database.db import db

# from datetime import datetime, timezone


from modules.usuarios_module.model import Usuario
from modules.perfil_cliente_module.model import PerfilCliente
from modules.prestamos_module.model import Prestamo
from modules.transacciones_module.model import Transaccion

app = create_app()

with app.app_context():
    # Elimina todas las tablas (opcional, para pruebas) y las crea de nuevo.
    db.drop_all()
    db.create_all()

    # Crear un usuario
    usuario = Usuario(
        nombre="Juan",
        apellido="Perez",
        tipo_documento="CC",
        num_documento="123456789",
        telefono="3001234567",
        direccion="Calle 123",
        email="juan.perez@example.com",
        username="juanp",
        password="hashedpassword",  # En producción, usa un hash (por ejemplo, bcrypt)
        rol="cliente",
        estado="ACTIVO"
    )
    db.session.add(usuario)
    db.session.commit()  # Para que se genere el ID
    
    # Crear el perfil del cliente asociado al usuario
    perfil = PerfilCliente(
        usuario_id=usuario.id_usuario,
        entidad_bancaria="Banco Nacional",
        tipo_cuenta="Ahorros",
        numero_cuenta="000111222",
        num_documento="123456789"
    )
    db.session.add(perfil)
    db.session.commit()


    # Crear un préstamo asociado al perfil del cliente
    prestamo = Prestamo(
        prestamo_codigo="P0001",
        tasa_interes=5.5,
        fecha_inicio="2025-01-01",
        fecha_final="2026-01-01",
        plazo_meses=12,
        estado="ACTIVO",
        monto_prestamo=10000.00,
        monto_intereses=550.00,
        total=10550.00,
        pagado=0,
        saldo_pendiente=10550.00,
        observacion="Primer préstamo",
        cliente_id=perfil.id_perfil_cliente
    )
    db.session.add(prestamo)
    db.session.commit()

    # Crear dos transacciones para el préstamo
    transaccion1 = Transaccion(
        monto=1000.00,
        tipo_transaccion="ABONO_CAPITAL",
        prestamo_id=prestamo.id_prestamo,
        usuario_id=usuario.id_usuario
    )
    transaccion2 = Transaccion(
        monto=500.00,
        tipo_transaccion="INTERES",
        prestamo_id=prestamo.id_prestamo,
        usuario_id=usuario.id_usuario
    )
    db.session.add(transaccion1)
    db.session.add(transaccion2)
    db.session.commit()

    print("Base de datos creada y datos de ejemplo insertados.")

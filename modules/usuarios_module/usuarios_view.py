from flask import Blueprint, render_template, request
from pydantic import ValidationError
from modules.usuarios_module.services import UsuarioService
from schemas.usuario import UsuarioCreate  # Para validar datos en el formulario

usuario_view_bp = Blueprint('usuario_view_bp', __name__, template_folder='templates/usuarios')
usuario_service = UsuarioService()

@usuario_view_bp.route('/usuarios/list', methods=['GET'])
def list_usuarios():
    # Obtiene todos los usuarios a través del servicio.
    # Nota: get_all_usuarios devuelve una lista de UsuarioRead (pydantic)
    usuarios = usuario_service.get_all_usuarios()
    # Renderizamos la plantilla pasándole la lista de usuarios
    return render_template('lista_usuarios.html', usuarios=usuarios)

@usuario_view_bp.route('/usuarios/<int:usuario_id>', methods=['GET'])
def detalle_usuario(usuario_id: int):
    # Obtiene el usuario por ID
    usuario = usuario_service.get_usuario_by_id(usuario_id)
    if usuario is None:
        # Si no se encuentra el usuario, renderizamos una plantilla de error
        return render_template('error.html', error="Usuario no encontrado")
    # Renderiza la plantilla de detalle con la información del usuario
    return render_template('detalle_usuario.html', usuario=usuario)

@usuario_view_bp.route('/usuarios/new', methods=['GET', 'POST'])
def crear_usuario():
    if request.method == 'POST':
        # Para formularios, extraemos la data con request.form.to_dict()
        data = request.form.to_dict()
        try:
            # Validamos la data con el esquema de creación
            usuario_create = UsuarioCreate(**data)
        except ValidationError as e:
            # En caso de error, se renderiza la plantilla de creación con los errores y la data ingresada
            return render_template('crear_usuario.html', errors=e.errors(), form_data=data)
        
        # Creamos el usuario a través del servicio
        usuario_creado = usuario_service.create_usuario(usuario_create)
        # Luego redirigimos a la vista de detalle (o a otra que prefieras)
        return render_template('detalle_usuario.html', usuario=usuario_creado)
    # Si es GET, simplemente renderizamos el formulario de creación
    return render_template('crear_usuario.html')

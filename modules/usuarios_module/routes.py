# routes/usuario_routes.py

from flask import Blueprint, request, jsonify
from pydantic import ValidationError
from modules.usuarios_module.services import UsuarioService
from schemas.usuario import UsuarioCreate, UsuarioUpdate

# Instancia del objeto bluprin con ruta usuarios (verificar si el url_prefix viene aca o en el app)
usuarios_bp = Blueprint('usuarios_bp', __name__, url_prefix='/usuarios')

# Importo la capa de servicio que se comunica con el repository para hacer solicitudes a la bd
usuario_service = UsuarioService()


@usuarios_bp.route('/', methods=['GET'])
def get_usuarios():
    usuarios = usuario_service.get_all_usuarios()
    # Cada objeto del servicio ya es un esquema UsuarioRead, usamos model_dump() para convertirlo a dict
    return jsonify([usuario.model_dump() for usuario in usuarios]), 200

@usuarios_bp.route('/<int:usuario_id>', methods=['GET'])
def get_usuario(usuario_id: int):
    usuario = usuario_service.get_usuario_by_id(usuario_id)
    
    if usuario is None:
        return jsonify({"error": "Usuario no encontrado"}), 404
    return jsonify(usuario.model_dump()), 200

@usuarios_bp.route('/', methods=['POST'])
def create_usuario():
    # Extraemos la data de los formularios enviados (form data)
    data = request.form.to_dict()
    try:
        # Validamos la data con el esquema UsuarioCreate
        usuario_create = UsuarioCreate(**data)
    except ValidationError as e:
        return jsonify({"errors": e.errors()}), 400

    usuario_creado = usuario_service.create_usuario(usuario_create)
    return jsonify(usuario_creado.model_dump()), 201

@usuarios_bp.route('/<int:usuario_id>', methods=['PUT'])
def update_usuario(usuario_id: int):
    data = request.form.to_dict()
    try:
        usuario_update = UsuarioUpdate(**data)
    except ValidationError as e:
        return jsonify({"errors": e.errors()}), 400

    usuario_actualizado = usuario_service.update_usuario(usuario_id, usuario_update)
    if usuario_actualizado is None:
        return jsonify({"error": "Usuario no encontrado"}), 404
    return jsonify(usuario_actualizado.model_dump()), 200

@usuarios_bp.route('/<int:usuario_id>', methods=['DELETE'])
def delete_usuario(usuario_id: int):
    eliminado = usuario_service.delete_usuario(usuario_id)
    if not eliminado:
        return jsonify({"error": "Usuario no encontrado"}), 404
    return jsonify({"message": "Usuario eliminado"}), 200

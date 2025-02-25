from typing import Optional, List, Dict, Any
from modules.usuarios_module.repository import UsuarioRepository
from modules.usuarios_module.model import Usuario
from schemas.usuario import UsuarioCreate,UsuarioRead,UsuarioUpdate 

class UsuarioService():
    def __init__(self) -> None:
        self.repository = UsuarioRepository()
    
    def get_all_usuarios(self) -> List[UsuarioRead]:
        usuarios = self.repository.get_all()
        # Se mapean los usuarios que traen el password a un objeto de Usuario read sin password
        return [UsuarioRead.model_validate(usuario) for usuario in usuarios]
        # return self.repository.get_all()
    
    def get_usuario_by_id(self, id_usuario : int) -> Optional[UsuarioRead]:
        usuario = self.repository.get_by_id(id_usuario)
        if usuario is None:
            return None
        return UsuarioRead.model_validate(usuario)
    
    def create_usuario(self, data: UsuarioCreate)-> UsuarioRead:

        usuario = Usuario( 
                        nombre = data.nombre, 
                        apellido = data.apellido, 
                        tipo_documento = data.tipo_documento,
                        num_documento = data.num_documento, 
                        telefono = data.telefono, 
                        direccion = data.direccion, 
                        email = data.email, 
                        username = data.username,
                        rol = data.rol,
                        estado = data.estado,
                        privilegio = data.privilegio,

                        password = data.password  # En producción, aplicar un hash (por ejemplo, bcrypt)
                        )
        # Se crea el usuario en la base de datos y se retorna el objeto UsuarioRead sin password
        usuario_creado = self.repository.create(usuario)
        return UsuarioRead.model_validate(usuario_creado)
        #return self.repository.create(usuario)
        # self.repository.create(usuario)
        # return UsuarioRead.from_orm(usuario)
    
    #! Corregir los campos del update
    def update_usuario(self, usuario_id: int, data: UsuarioUpdate) -> Optional[UsuarioRead]:
        usuario = self.repository.get_by_id(usuario_id)  # Usar self.repository, no self.repo
        if not usuario:
            return None
        if data.nombre is not None:
            usuario.nombre = data.nombre
        if data.apellido is not None:
            usuario.apellido = data.apellido
        if data.tipo_documento is not None:
            usuario.tipo_documento = data.tipo_documento
        if data.num_documento is not None:
            usuario.num_documento = data.num_documento
        if data.telefono is not None:
            usuario.telefono = data.telefono
        if data.direccion is not None:
            usuario.direccion = data.direccion
        if data.email is not None:
            usuario.email = data.email
        if data.username is not None:
            usuario.username = data.username
        if data.password is not None:
            usuario.password = data.password
        if data.rol is not None:
            usuario.rol = data.rol
        if data.estado is not None:
            usuario.estado = data.estado
        if data.privilegio is not None:
            usuario.privilegio = data.privilegio
        # Se almacena a la base de datos el usuario actualizado y se devuelve el objeto sin password
        self.repository.update(usuario)
        return UsuarioRead.model_validate(usuario)


    def delete_usuario(self, usuario_id: int) -> bool:
            usuario = self.repository.get_by_id(usuario_id)
            if not usuario:
                return False
            self.repository.delete(usuario)
            return True
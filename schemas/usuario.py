# schemas/usuario.py
from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional

class UsuarioBase(BaseModel):
    nombre: str
    apellido: str
    tipo_documento: str
    num_documento: str
    telefono: Optional[str] = None
    direccion: Optional[str] = None
    email: EmailStr
    username: str
    rol: str
    estado: Optional[str] = 'ACTIVO'
    privilegio: Optional[str] = None

    #! Solucion 1
    model_config = ConfigDict(from_attributes=True)
    #! Solucion 1
    #class Config:
        #from_attributes = True
        # orm_mode = True
        #! Deprecada esta opcion
        # orm_mode permite crear instancias de este esquema a partir de objetos ORM (por ejemplo, Usuario)



class UsuarioCreate(UsuarioBase):
    password: str  # Requerido al crear el usuario

class UsuarioRead(UsuarioBase):
    id_usuario: int  # Se incluye el identificador para la lectura; no se expone el password

class UsuarioUpdate(BaseModel):
    nombre: Optional[str] = None
    apellido: Optional[str] = None
    tipo_documento: Optional[str] = None
    num_documento: Optional[str] = None
    telefono: Optional[str] = None
    direccion: Optional[str] = None
    email: Optional[EmailStr] = None
    username: Optional[str] = None
    password: Optional[str] = None
    rol: Optional[str] = None
    estado: Optional[str] = None
    privilegio: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


""" 
Para convertirlo a dict, ya no se usa .dict() sino .model_dump(), 
aunque .dict() sigue existiendo como alias de compatibilidad. 
La forma oficial en Pydantic 2.x es:

data_dict = usuario_read.model_dump()

"""
from .model import Usuario
from database.db import db
from typing import List, Optional

class UsuarioRepository:
    def get_all(self) -> List[Usuario]:
        return Usuario.query.all()

    def get_by_id(self, usuario_id: int) -> Optional[Usuario]:
        return Usuario.query.get(usuario_id)

    def create(self, usuario: Usuario ) -> Usuario:
        db.session.add(usuario)
        db.session.commit()
        return usuario

    def update(self, usuario: Usuario) -> Usuario:
        db.session.commit()
        return usuario

    def delete(self, usuario) -> None:
        db.session.delete(usuario)
        db.session.commit()

from database import db
from datetime import datetime

class Tarefa(db.Model):
    __tablename__ = 'tarefas'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(120), nullable=False)
    descricao = db.Column(db.String(255))
    concluida = db.Column(db.Boolean, default=False)
    data = db.Column(db.DateTime, default=datetime.utcnow)

    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)

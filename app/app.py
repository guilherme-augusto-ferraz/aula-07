from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from database import db

bcrypt = Bcrypt()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)

    # Configurações do app
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'chave-super-secreta'  # troque em produção

    # Inicialização das extensões
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # Importação dos models (importante para o SQLAlchemy reconhecer as tabelas)
    from models.usuario import Usuario
    from models.tarefa import Tarefa

    # Registro das rotas
    from routes.usuarios import usuarios_bp
    from routes.tarefas import tarefas_bp

    app.register_blueprint(usuarios_bp, url_prefix='/api/usuarios')
    app.register_blueprint(tarefas_bp, url_prefix='/api/tarefas')

    with app.app_context():
        db.create_all()

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

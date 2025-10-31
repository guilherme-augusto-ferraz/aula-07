from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from database import db
from models.usuario import Usuario

usuarios_bp = Blueprint('usuarios', __name__)

# Registro de usuário
@usuarios_bp.route('/cadastro', methods=['POST'])
def cadastro():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Usuário e senha são obrigatórios'}), 400

    if Usuario.query.filter_by(username=username).first():
        return jsonify({'error': 'Usuário já existe'}), 400

    usuario = Usuario(username=username)
    usuario.set_password(password)
    db.session.add(usuario)
    db.session.commit()

    return jsonify({'message': 'Usuário criado com sucesso'}), 201


# Login e geração de token JWT
@usuarios_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    usuario = Usuario.query.filter_by(username=username).first()
    if not usuario or not usuario.check_password(password):
        return jsonify({'error': 'Credenciais inválidas'}), 401

    token = create_access_token(identity=str(usuario.id))
    return jsonify({'token': token}), 200

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from database import db
from models.tarefa import Tarefa

tarefas_bp = Blueprint('tarefas', __name__)

# Criar uma nova tarefa
@tarefas_bp.route('/create', methods=['POST'])
@jwt_required()
def create_tarefa():
    usuario_id = int(get_jwt_identity())
    data = request.get_json()
    titulo = data.get('titulo')
    descricao = data.get('descricao', '')

    if not titulo:
        return jsonify({'error': 'Título é obrigatório'}), 400

    tarefa = Tarefa(titulo=titulo, descricao=descricao, usuario_id=usuario_id)
    db.session.add(tarefa)
    db.session.commit()

    return jsonify({'message': 'Tarefa criada com sucesso', 'id': tarefa.id}), 201


# Listar tarefas do usuário logado
@tarefas_bp.route('/', methods=['GET'])
@jwt_required()
def list_tarefas():
    usuario_id = get_jwt_identity()
    tasks = Tarefa.query.filter_by(usuario_id=usuario_id).all()
    result = [
        {
            'id': t.id,
            'titulo': t.titulo,
            'descricao': t.descricao,
            'concluida': t.concluida,
            'data': t.data.isoformat()
        } for t in tasks
    ]
    return jsonify(result), 200


# Atualizar tarefa
@tarefas_bp.route('/<int:tarefa_id>', methods=['PUT'])
@jwt_required()
def update_tarefa(tarefa_id):
    usuario_id = get_jwt_identity()
    tarefa = Tarefa.query.filter_by(id=tarefa_id, usuario_id=usuario_id).first()

    if not tarefa:
        return jsonify({'error': 'Tarefa não encontrada'}), 404

    data = request.get_json()
    tarefa.titulo = data.get('titulo', tarefa.titulo)
    tarefa.descricao = data.get('descricao', tarefa.descricao)
    tarefa.concluida = data.get('concluida', tarefa.concluida)

    db.session.commit()
    return jsonify({'message': 'Tarefa atualizada com sucesso'}), 200


# Deletar tarefa
@tarefas_bp.route('/<int:tarefa_id>', methods=['DELETE'])
@jwt_required()
def delete_tarefa(tarefa_id):
    usuario_id = get_jwt_identity()
    tarefa = Tarefa.query.filter_by(id=tarefa_id, usuario_id=usuario_id).first()

    if not tarefa:
        return jsonify({'error': 'Tarefa não encontrada'}), 404

    db.session.delete(tarefa)
    db.session.commit()
    return jsonify({'message': 'Tarefa excluída com sucesso'}), 200

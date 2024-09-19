from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import Document
from datetime import datetime

bp = Blueprint('document', __name__)

@bp.route('/documents', methods=['GET', 'POST'])
@jwt_required()
def documents():
    user_id = get_jwt_identity()

    if request.method == 'GET':
        docs = Document.objects(user_id=user_id)
        return jsonify([doc.to_json() for doc in docs])
    
    if request.method == 'POST':
        data = request.get_json()
        doc = Document(
            title=data['title'],
            content=data['content'],
            user_id=user_id,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        doc.save()
        return jsonify(doc.to_json()), 201

@bp.route('/documents/<doc_id>', methods=['GET', 'PUT', 'DELETE'])
@jwt_required()
def document(doc_id):
    user_id = get_jwt_identity()
    doc = Document.objects(id=doc_id, user_id=user_id).first()

    if not doc:
        return jsonify({"message": "Document not found"}), 404

    if request.method == 'GET':
        return jsonify(doc.to_json())
    
    if request.method == 'PUT':
        data = request.get_json()
        doc.title = data.get('title', doc.title)
        doc.content = data.get('content', doc.content)
        doc.updated_at = datetime.utcnow()
        doc.save()
        return jsonify(doc.to_json())
    
    if request.method == 'DELETE':
        doc.delete()
        return jsonify({"message": "Document deleted successfully"})

from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import User

bp = Blueprint('user', __name__)

@bp.route('/profile', methods=['GET', 'PUT'])
@jwt_required()
def profile():
    user_id = get_jwt_identity()
    user = User.objects(id=user_id).first()

    if request.method == 'GET':
        return jsonify({
            "email": user.email,
            "name": user.name,
            "dream_college": user.dream_college
        })
    
    if request.method == 'PUT':
        data = request.get_json()
        user.name = data.get('name', user.name)
        user.dream_college = data.get('dream_college', user.dream_college)
        user.save()
        return jsonify({"message": "Profile updated successfully"})

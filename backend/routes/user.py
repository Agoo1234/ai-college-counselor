from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.user import User, db

bp = Blueprint('user', __name__)

@bp.route('/profile', methods=['GET', 'PUT'])
@jwt_required()
def profile():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    if not user:
        return jsonify({"message": "User not found"}), 404

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
        db.session.commit()
        return jsonify({"message": "Profile updated successfully"})

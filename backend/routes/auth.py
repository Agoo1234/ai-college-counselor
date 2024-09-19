from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from models import User

bp = Blueprint('auth', __name__)

@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    user = User(email=data['email'], name=data['name'], dream_college=data['dream_college'])
    user.set_password(data['password'])
    user.save()
    return jsonify({"message": "User registered successfully"}), 201

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.objects(email=data['email']).first()
    if user and user.check_password(data['password']):
        access_token = create_access_token(identity=str(user.id))
        return jsonify(access_token=access_token), 200
    return jsonify({"message": "Invalid credentials"}), 401

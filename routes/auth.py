from flask import Blueprint, request, jsonify
from models.user import User, UserAuthentication
from extensions import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    email = request.json.get('email')
    username = request.json.get('username')
    password = request.json.get('password')
    # Add registration logic here
    return jsonify({"message": "User registered"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')
    # Add login logic here
    return jsonify({"message": "User logged in"}), 200

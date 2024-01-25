from flask import Blueprint, request
from utils import response_error, response_success
from app.models.users import User
from app.crypt import bcrypt
from sqlalchemy.exc import IntegrityError
from app.models.tasks import Task
from app.db import db
from flask_jwt_extended import create_access_token, jwt_required
from datetime import timedelta


user_route = Blueprint('user_route', __name__)


@user_route.route("/users")
@jwt_required()
def get_users():
    try:
        users = User.query.all()
        serialized_users = [user.to_json() for user in users]
        return response_success(serialized_users)
    except Exception as e:
        return response_error(str(e))
    

@user_route.route("/users/<int:user_id>")
@jwt_required()
def get_user(user_id):
    result = User.query.get(user_id)

    if result is None: 
        return response_error("User not found")
    
    return response_success(result.to_json())
    

@user_route.route("/users", methods=["POST"])
def add_user():
    try:
        user = User(**request.get_json())
        user.password = bcrypt.generate_password_hash(user.password)
        db.session.add(user)
        db.session.commit()

        return response_success("Usuario creado correctamente", 201)
    except IntegrityError:
        return response_error("Nombre de usuario o email ya existentes")
    except Exception as e:
        return response_error(str(e))
    

@user_route.route("/users/<int:user_id>", methods=["PUT"])
@jwt_required()
def update_user(user_id):
    try:
        user = User.query.get(user_id)

        if user is None:
            return response_error("User not found")
        
        new_user = request.json
        user.name = new_user.get("name", user.name)
        user.lastname = new_user.get("lastname", user.lastname)
        user.username = new_user.get("username", user.username)
        user.phone = new_user.get("phone", user.phone)
        user.address = new_user.get("address", user.address)
        user.email = new_user.get("email", user.email)
        user.username = new_user.get("username", user.username)

        db.session.commit()

        return response_success("Usuario actualizado correctamente")
    except Exception as e:
        return response_error(str(e))


@user_route.route("/users/<int:user_id>", methods=["DELETE"])
@jwt_required()
def delete_user(user_id):
    try:
        tasks_by_user = Task.query.filter_by(user_id=user_id).all()

        if len(tasks_by_user) is 0:
            user = User.query.get(user_id)

            if user is None:
                return response_error("User not found")
            
            db.session.delete(user)
            db.session.commit()
            return response_success("Usuario eliminado correctamente")
        return response_success("El usuario no puede ser eliminado porque tiene tareas pendientes")
    
    except Exception as e:
        return response_error(str(e))
    

@user_route.route("/login", methods=['POST'])
def login():
    try:
        body = request.get_json()
        email = body.get("email")
        password = body.get("password")

        user = User.query.filter_by(email=email).first()

        if not user:
            return response_error("Email y/o password incorrectos")
        
        if not bcrypt.check_password_hash(user.password, password):
            return response_error("Email y/o password incorrectos")
        

        # duración del token por defecto: 15 min
        token = create_access_token(identity=user.email, expires_delta=timedelta(weeks=2))
        return response_success({
            'user': user.to_json(),
            'access_token': token
        })
    except Exception as e:
        return response_error(str(e))
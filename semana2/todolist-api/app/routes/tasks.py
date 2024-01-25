from flask import Blueprint, request
from utils import response_error, response_success
from app.models.tasks import Task
from app.db import db
from flask_jwt_extended import jwt_required


task_route = Blueprint('task_route', __name__)


# Se pueden crear rutas :p // Para obtener puerto y tener vista previa:
# python app.py (archivo) 
# @task_route.route("/") # "/" --> Ruta raíz
# def hola_mundo(): # def function():
#    #return "Hola mundo"  # al entrar a la ruta raíz, se ejecutará hola_mundo
#     return response_success("Hola mundo")


@task_route.route("/tasks/<int:user_id>")
@jwt_required()
def get_tasks(user_id):
    try:
        tasks = Task.query.filter_by(user_id=user_id)
        # comprehesion (for en una línea)
        serialized_tasks = [task.to_json() for task in tasks]

        return response_success(serialized_tasks)
    except Exception as e:
        return response_error(str(e))


@task_route.route("/tasks/<int:task_id>")
@jwt_required()
def get_task(task_id):
    try:
        result = Task.query.get(task_id)

        if result is None: 
            return response_error("Task not found")
        
        return response_success(result.to_json())
    except Exception as e:
        return response_error(str(e))


@task_route.route("/tasks", methods=["POST"])
@jwt_required()
def add_task():
    try:
        task = Task(**request.get_json())
        db.session.add(task)
        db.session.commit()
        return response_success("Tarea creada correctamente", 201)
    except Exception as e:
        return response_error(str(e))


@task_route.route("/tasks/<int:task_id>", methods=["PUT"])
@jwt_required()
def update_task(task_id):
    # Buscar tarea por id
    try:
        task = Task.query.get(task_id)

        # Se valida si task es None -> retorna ese response
        if task is None:
            return response_error("Task not found")
        
        # Si existe -> se obtiene el json que envía postman
        new_task = request.json #el json que envía postman
        task.title = new_task.get("title", task.title)
        task.category = new_task.get("category", task.category)        
        task.priority = new_task.get("priority", task.priority)
        task.status = new_task.get("status", task.status)        
        task.is_done = new_task.get("is_done", task.is_done)
        task.due_date = new_task.get("due_date", task.due_date)
        task.user_id = new_task.get("user_id", task.user_id)

        db.session.commit()

        return response_success("Tarea actualizada correctamente")
    except Exception as e:
        return response_error(str(e))


@task_route.route("/tasks/<int:task_id>", methods=["DELETE"])
@jwt_required()
def delete_task(task_id):
    try:
        task = Task.query.get(task_id)

        if task is None:
            return response_error("Task not found")
        
        db.session.delete(task)
        db.session.commit()
        return response_success("Tarea eliminada correctamente")
    except Exception as e:
        return response_error(str(e))
from flask import jsonify, request
from app.models import Task

from datetime import date

def index():
    return jsonify(
        {
            'mensaje': 'Hola Mundo Listado de tareas'
        }
    )

def get_task(task_id):
    task = Task.get_by_id(task_id)
    if not task:
        return jsonify({'message': 'Task not found'}), 404
    return jsonify(task.serialize())

def create_task():
    data = request.json
    new_task = Task(
        nombre=data['nombre'],
        genero = data['genero'],
        fecha = data['fecha'],
        foto= data['foto']
    )
    new_task.save()
    return jsonify({'message': 'Task created successfully'}), 201


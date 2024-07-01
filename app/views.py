from flask import jsonify, request
from app.models import Banda

from datetime import date

def index():
    return jsonify(
        {
            'mensaje': 'Hola Mundo Listado de tareas'
        }
    )

def get_all():
    bands = Banda.get_all()
    print(bands)
    return jsonify([band.serialize() for band in bands])

def get_band(task_id):
    band = Banda.get_by_id(task_id)
    if not band:
        return jsonify({'message': 'Task not found'}), 404
    return jsonify(band.serialize())

def create_band():
    data = request.json
    new_band = Banda(
        nombre=data['nombre'],
        genero = data['genero'],
        fecha = data['fecha'],
        foto= data['foto']
    )
    new_band.save()
    return jsonify({'message': 'Band created successfully'}), 201


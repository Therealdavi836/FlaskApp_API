
#Practica de flask creando una API para usuarios
import math
from flask import Flask, jsonify, request

app = Flask(__name__)

#Creamos un diccionario en memoria para probar los metodos get post put y delete
usuarios = [
    {"id": 1, "nombre": "Juan", "edad": 22},
    {"id": 2, "nombre": "Ana", "edad": 25}
]

# GET: crear metodo get para recibir a los usuarios
@app.route('/get_usuarios', methods=['GET'])
def get_usuarios():
    return jsonify(usuarios)

# POST: crear un nuevo usuario
@app.route("/crear_usuarios", methods=["POST"])
def crear_usuarios():
    data = request.get_json()
    #condicional de usuarios
    nuevo_id = usuarios[-1]["id"] + 1 if usuarios else 1 #condicional ternario
    #creamos el formato de JSON a enviar
    nuevo_usuario = {
        "id": nuevo_id,
        "nombre": data.get("nombre"),
        "edad": data.get("edad")
    }
    usuarios.append(nuevo_usuario)
    return jsonify({"mensaje": "Usuario creado", "usuario": nuevo_usuario}), 201

# PUT: actualizar usuario por id
@app.route("/actualizar_usuarios/<int:usuario_id>", methods=["PUT"])
def actualizar_usuarios(usuario_id):
    data = request.get_json()
    for usuario in usuarios:
        if usuario["id"] == usuario_id:
            usuario["nombre"] = data.get("nombre", usuario["nombre"])
            usuario["edad"] = data.get("edad", usuario["edad"])
            return jsonify({"mensaje": "Usuario actualizado", "usuario": usuario})
    return jsonify({"mensaje": "Usuario no encontrado"}), 404


# DELETE: eliminar usuario por id
@app.route("/eliminar_usuarios/<int:usuario_id>", methods=["DELETE"])
def eliminar_usuarios(usuario_id):
    for usuario in usuarios:
        if usuario["id"] == usuario_id:
            usuarios.remove(usuario)
            return jsonify({"mensaje": "Usuario eliminado"})
    return jsonify({"mensaje": "Usuario no encontrado"}), 404
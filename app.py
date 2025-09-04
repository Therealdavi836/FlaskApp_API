# Primera practica Creacion de una API en Flask de python
#Importamos flask, metodo jsonify para convertir a json, request para traer datos del json y math para sqrt
from flask import Flask, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client["Divisas"]
divisas_collection = db["Valor_Divisas"]

#Metodo divisas para agregarlas en la base de datos
@app.route('/divisas', methods=['POST'])
def agregar_divisas():
    data = request.get_json()
    result = divisas_collection.insert_one({
        "origen":data["origen"],
        "destino":data["destino"],
        "valor":float(data["valor"])
    })
    return jsonify({
        "mensaje": "Divisa guardada correctamente",
        "id": str(result.inserted_id)
    }), 201
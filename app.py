# Primera practica Creacion de una API en Flask de python
#Importamos flask, metodo jsonify para convertir a json, request para traer datos del json y math para sqrt
import math
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

#Indice por defecto
@app.route('/')
def index():
    return 'Index Page'

#Creando un nuevo metodo sumar 
@app.route("/sumar")
def sumar():
    resultado = 2 + 2
    return jsonify(resultado)

#Recibir valor especifica el metodo POST para enviar datos
@app.route('/recibir_valor', methods=['POST'])
def recibir_valor():

    dato = request.get_json()
    digito = dato.get('valor')
    numero = digito + 1
    raiz_cuadrada = math.sqrt(numero)
    return jsonify(raiz_cuadrada)
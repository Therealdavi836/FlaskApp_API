# Primera practica Creacion de una API en Flask de python
#Importamos flask, metodo jsonify para convertir a json, request para traer datos del json y math para sqrt
import math
from flask import Flask, jsonify, request

app = Flask(__name__)

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
# Primera practica Creacion de una API en Flask de python
#Importamos flask, metodo jsonify para convertir a json, request para traer datos del json y math para sqrt
from flask import Flask, jsonify, request #Imports de los elementos de Flask
from pymongo import MongoClient #Importamos la conexion con la db

#definimos el app por el cual Flask funcionara
app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/") #Conexion con la base de datos
db = client["Divisas"]#traemos la base de datos de divisas
divisas_collection = db["Valor_Divisas"]#Definimos especificamente el documento donde iran los registros

#Metodo divisas para agregarlas en la base de datos, usando POST
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

#Tasas de cambio como ejemplificacion para convertir las divisas
#Usando referencia general el dolar
tasas_cambio = {
    
    "USD": 1,

    "COP": 3999.59,
    
    "MXN": 18.72,
    
    "EUR": 0.86
    
}

#Metodo convertir para hacer una conversion entre la moneda de origen y la moneda destino, en este caso es con base al dolar
@app.route('/convertir', methods=['POST'])
def convertir_divisas():

    #Extracción de los valores para mejorar la respuesta impresa
    data = request.get_json()
    origen = data.get("divisa_origen")
    destino = data.get("divisa_destino")
    valor = data.get("valor")

    #Si el origen/destino no esta en el diccionario creado por defecto, lanza 400 como respuesta de servidor
    if origen not in tasas_cambio or destino not in tasas_cambio:
        return jsonify({"error": "Moneda no soportada"}), 400
    
    #Extraccion de las monedas de origen y destino
    tasa_origen = tasas_cambio[origen]
    tasa_destino = tasas_cambio[destino]

    #Formula para convertir la tasa origen a su destino
    resultado = valor * (tasa_destino/tasa_origen)

    #devolvemos un JSON con los datos solicitados
    return jsonify({
        "Divisa origen": origen,
        "Divisa destino": destino,
        "Valor a convertir": valor,
        "Valor obtenido de la conversión": round(resultado, 2)
    }), 200
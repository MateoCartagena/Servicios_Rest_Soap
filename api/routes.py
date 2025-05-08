from flask import Blueprint, request, jsonify
from api.temperature import convertir_temperatura

api_blueprint = Blueprint('api', __name__)

zonas = {}

@api_blueprint.route('/zonas', methods=['POST'])
def registrar_zona():
    """
    Registrar una nueva zona agrícola.
    ---
    parameters:
      - name: nombre
        in: body
        required: true
        type: string
      - name: cultivo_principal
        in: body
        required: true
        type: string
      - name: hectareas
        in: body
        required: true
        type: number
      - name: coordenadas
        in: body
        required: true
        type: object
        properties:
          latitud:
            type: number
          longitud:
            type: number
    responses:
      201:
        description: Zona registrada exitosamente
    """
    data = request.get_json()
    id_zona = len(zonas) + 1
    zonas[id_zona] = data
    print(f"✅ Zona registrada: ID={id_zona}, Datos={data}")
    return jsonify({"id": id_zona, **data}), 201

@api_blueprint.route('/zonas', methods=['GET'])
def obtener_zonas():
    """
    Obtener todas las zonas registradas.
    ---
    responses:
      200:
        description: Lista de zonas registradas
    """
    print(f"📥 Se solicitó la lista de zonas. Total: {len(zonas)}")
    return jsonify(zonas)

@api_blueprint.route('/zonas/<int:id>', methods=['GET'])
def obtener_zona(id):
    """
    Obtener los datos de una zona específica.
    ---
    parameters:
      - name: id
        in: path
        required: true
        type: integer
    responses:
      200:
        description: Datos de la zona
      404:
        description: Zona no encontrada
    """
    zona = zonas.get(id)
    if zona:
        print(f"📍 Zona encontrada: ID={id}")
        return jsonify(zona)
    print(f"⚠️ Zona no encontrada: ID={id}")
    return jsonify({"error": "Zona no encontrada"}), 404

@api_blueprint.route('/zonas/<int:id>', methods=['DELETE'])
def eliminar_zona(id):
    """
    Eliminar una zona registrada.
    ---
    parameters:
      - name: id
        in: path
        required: true
        type: integer
    responses:
      200:
        description: Zona eliminada exitosamente
      404:
        description: Zona no encontrada
    """
    if id in zonas:
        del zonas[id]
        print(f"🗑️ Zona eliminada: ID={id}")
        return jsonify({"message": "Zona eliminada"}), 200
    print(f"⚠️ Intento de eliminar zona inexistente: ID={id}")
    return jsonify({"error": "Zona no encontrada"}), 404

@api_blueprint.route('/temperatura/convertir', methods=['GET'])
def convertir_temperatura_endpoint():
    """
    Convertir temperatura de Celsius a Fahrenheit usando un servicio SOAP.
    ---
    parameters:
      - name: valor
        in: query
        required: true
        type: number
        description: Valor en grados Celsius
    responses:
      200:
        description: Conversión a Fahrenheit
        schema:
          type: object
          properties:
            celsius:
              type: number
            fahrenheit:
              type: number
      400:
        description: Error, no se proporcionó valor en Celsius
    """
    celsius = request.args.get('valor', type=float)
    if celsius is None:
        return jsonify({"error": "Se debe proporcionar un valor en Celsius"}), 400

    fahrenheit = convertir_temperatura(celsius)
    print(f"🌡️ Conversión realizada: {celsius}°C = {fahrenheit}°F")

    return jsonify({
        "celsius": celsius,
        "fahrenheit": fahrenheit
    })

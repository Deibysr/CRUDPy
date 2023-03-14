# Instalar Flask
# pip install Flask

from flask import Flask, jsonify, request

app = Flask(__name__)

# Creamos una lista con algunos datos de ejemplo
datos = []

# Definimos la ruta para obtener todos los datos
@app.route('/datos', methods=['GET'])
def obtener_datos():
    return jsonify(datos)

# Definimos la ruta para obtener un dato en particular
@app.route('/datos/<int:id>', methods=['GET'])
def obtener_dato(id):
    for dato in datos:
        if dato['id'] == id:
            return jsonify(dato)
    return jsonify({'mensaje': 'Dato no encontrado'})

# Definimos la ruta para agregar un dato
@app.route('/datos', methods=['POST'])
def agregar_dato():
    nuevo_dato = request.get_json()
    datos.append(nuevo_dato)
    return jsonify({'mensaje': 'Dato agregado correctamente'})

# Definimos la ruta para actualizar un dato
@app.route('/datos/<int:id>', methods=['PUT'])
def actualizar_dato(id):
    for dato in datos:
        if dato['id'] == id:
            dato['nombre'] = request.json['nombre']
            dato['edad'] = request.json['edad']
            return jsonify({'mensaje': 'Dato actualizado correctamente'})
    return jsonify({'mensaje': 'Dato no encontrado'})

# Definimos la ruta para eliminar un dato
@app.route('/datos/<int:id>', methods=['DELETE'])
def eliminar_dato(id):
    for dato in datos:
        if dato['id'] == id:
            datos.remove(dato)
            return jsonify({'mensaje': 'Dato eliminado correctamente'})
    return jsonify({'mensaje': 'Dato no encontrado'})

if __name__ == '__main__':
    app.run(debug=True)

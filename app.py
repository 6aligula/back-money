from flask import Flask, request, jsonify
from datetime import datetime
import json

app = Flask(__name__)

@app.route('/saveData', methods=['POST'])
def save_data():
    data = request.get_json()  # obtener los datos enviados en la solicitud POST
    if not data:
        return jsonify({'message': 'No data provided'}), 400

    try:
        # Convierte el primer id en un objeto datetime (asumiendo que el id es un timestamp en milisegundos)
        date = datetime.fromtimestamp(data[0]['value'][0]['id'] / 1000)  
        # Extrae el año y el mes del objeto datetime
        year = date.year
        month = date.strftime('%B')

        # Genera el nombre del archivo usando el año y el mes
        file_name = f'{month}_{year}.json'

        with open(file_name, 'w') as f:  # abre el archivo con el nombre generado en modo de escritura
            json.dump(data, f)  # escribe los datos en el archivo
        return jsonify({'message': 'Data saved successfully'}), 200
    except Exception as e:
        return jsonify({'message': 'An error occurred while saving data: ' + str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

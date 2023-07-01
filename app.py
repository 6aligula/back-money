from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/saveData', methods=['POST'])
def save_data():
    data = request.get_json()  # obtener los datos enviados en la solicitud POST
    if not data:
        return jsonify({'message': 'No data provided'}), 400

    try:
        with open('data.json', 'w') as f:  # abre el archivo data.json en modo de escritura
            json.dump(data, f)  # escribe los datos en el archivo
        return jsonify({'message': 'Data saved successfully'}), 200
    except Exception as e:
        return jsonify({'message': 'An error occurred while saving data: ' + str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)  # corre el servidor en la dirección y puerto especificados

from flask import Flask, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)

@app.route('/saveData', methods=['POST'])
def save_data():
    data = request.get_json()  # obtener los datos enviados en la solicitud POST
    if not data:
        return jsonify({'message': 'No data provided'}), 400

    # Get month and year from the data
    try:
        # Assuming the 'id' field is a timestamp
        timestamp = data[0]['value'][0]['id']
        date = datetime.fromtimestamp(timestamp/1000)  # Convert timestamp to seconds
        month = date.strftime('%B')
        year = date.year

        filename = f'{month}_{year}.json'  # This will give a filename like 'July_2023.json'
    except KeyError:
        return jsonify({'message': 'Invalid data format'}), 400
    except Exception as e:
        return jsonify({'message': 'An error occurred while processing data: ' + str(e)}), 400

    try:
        with open(filename, 'w') as f:  # abre el archivo en modo de escritura
            json.dump(data, f)  # escribe los datos en el archivo
        return jsonify({'message': 'Data saved successfully'}), 200
    except Exception as e:
        return jsonify({'message': 'An error occurred while saving data: ' + str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

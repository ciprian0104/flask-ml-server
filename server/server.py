from flask import Flask, request, jsonify
import loading_helper

app = Flask(__name__)


# Ruta la care asculta aplicația noastra

@app.route('/predict_price', methods=['POST'])
def get_price():

    # Parametrii care ii vom trimite modelului nostru salvat. 

    address = request.form['zone']

    rooms = int(request.form['bedrooms'])
    
    sqmt = float(request.form['sqmt'])
    
    level = int(request.form['floor'])
    
    level_max = int(request.form['number_of_floors'])

    baths = int(request.form['baths'])

    # Returnam aplicatiei noastre rezultatul modelului nostru și il transformam in format JSON

    response = jsonify({
        'estimated_price': loading_helper.get_property_price(address, rooms, sqmt, level, level_max, baths)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

# Linie de cod care este tot timpul adevarata si este folosita pentru a incepe rularea serverului nostru
if __name__ == "__main__":
    print("Starting Flask Prediction Service...")
    loading_helper.load_saved_model()
    app.run()


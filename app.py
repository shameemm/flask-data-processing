
from flask import Flask, jsonify, request
from flask import Response

app = Flask(__name__)

# In-memory storage for processed data
processed_data = {}

# Mock data to simulate fetching from an external service
mock_data = {
    "data": [
        "Guerilla",
        "Himalayan",
        "Shotgun",
        "Meteor"
    ]
}

@app.route('/fetch-data', methods=['GET'])
def fetch_data():
    # Simulate fetching data from an external service
    return jsonify(mock_data)

@app.route('/process-data', methods=['POST'])
def process_data():
    global processed_data
    
    # Get data from the request
    data = request.json.get('data', [])
    
    # Simple data processing: convert all text to uppercase
    processed_data['processed'] = [item.upper() for item in data]
    
    return jsonify({"message": "Data processed successfully"})

@app.route('/get-processed-data', methods=['GET'])
def get_processed_data():
    # Return the processed data stored in memory
    return jsonify(processed_data)

if __name__ == '__main__':
    app.run(debug=True)
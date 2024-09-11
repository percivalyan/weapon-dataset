from flask import Flask, jsonify
import json

app = Flask(__name__)

# Load JSON data
with open('weapon-dataset.json') as f:
    data = json.load(f)

@app.route('/api/weapons', methods=['GET'])
def get_weapons():
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

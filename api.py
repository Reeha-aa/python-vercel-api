from flask import Flask, request, jsonify
from flask_cors import CORS
import json

# Load the marks from the JSON file
with open("python-vercel.json") as f:
    student_data = json.load(f)

app = Flask(__name__)
CORS(app)  # Enable CORS

@app.route('/api', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')  # Get the names from the query parameters
    marks = [student_data.get(name, 0) for name in names]  # Get marks for each name
    return jsonify({"marks": marks})

if __name__ == "__main__":
    app.run()

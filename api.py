from flask import Flask, request, jsonify
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for GET requests from any origin

# Load the marks data from marks.json
with open("marks.json") as f:
    student_data = json.load(f)

@app.route('/api', methods=['GET'])
def get_marks():
    # Get the names from the query parameters
    names = request.args.getlist('name')
    
    # Find the marks for the requested names
    marks = [next((student['marks'] for student in student_data if student['name'] == name), None) for name in names]
    
    return jsonify({"marks": marks})
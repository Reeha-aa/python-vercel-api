from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Load student data from the JSON file.  Convert to a dictionary for faster lookups.
try:
    with open("marks.json", "r") as f:
        student_list = json.load(f)
        student_data = {student["name"]: student["marks"] for student in student_list}  # Create dictionary
except FileNotFoundError:
    print("Error: marks.json not found.")
    exit(1)

@app.route("/api")
def get_marks():
    names = request.args.getlist("name")
    marks = []

    for name in names:
        marks.append(student_data.get(name, None)) # Use .get() to handle missing names efficiently.

    response = {"marks": marks}
    return jsonify(response)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET')
    return response

if __name__ == "__main__":
    app.run(debug=True, port=5000)
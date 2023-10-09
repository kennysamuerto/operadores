from flask import Flask, request, jsonify, render_template
import csv

app = Flask(__name__)

def extract_operator_lines_case_insensitive(file_path, operator_name):
    extracted_lines = []
    with open(file_path, 'r', encoding='ISO-8859-1') as file:
        for line in file:
            if operator_name.lower() in line.lower():
                extracted_lines.append(line.strip().split('#'))
    return extracted_lines

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/search', methods=['POST'])
def search():
    data = request.json
    print("Data received:", data)  # Debugging
    operator_name = data.get('operator_name', '')
    print("Operator name:", operator_name)  # Debugging
    file_path = "/ruta/archivo/operadores/Geografico.txt"
    results = extract_operator_lines_case_insensitive(file_path, operator_name)
    print("Search results:", results)  # Debugging
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)



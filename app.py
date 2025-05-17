from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Almacenamiento temporal
ultimos_datos = {}

@app.route('/')
def index():
    return render_template("index.html", datos=ultimos_datos)

@app.route('/api/datos', methods=['POST'])
def recibir_datos():
    global ultimos_datos
    datos = request.get_json()
    print("Datos recibidos:", datos)
    ultimos_datos = datos
    return jsonify({"status": "ok", "message": "Datos recibidos"}), 200

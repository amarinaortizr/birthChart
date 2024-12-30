#!/usr/bin/env python
from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

"""
sol
luna
ascendente
planetas
quiron
casas
"""


# Banco de palabras para el autocompletado
#signos = ["Aries", "Tauro", "Géminis", "Cáncer", "Leo", "Virgo", "Libra", "Escorpio", "Sagitario", "Capricornio", "Acuario", "Piscis"]
signos = ["Aries", "Acuario", "Cancer", "Capricornio", "Escorpio", "Géminis", "Leo", "Libra", "Piscis" ,  "Sagitario", "Tauro",  "Virgo"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/autocomplete", methods=["GET"])
def autocomplete():
    query = request.args.get("q", "").lower()  # Convierte la consulta a minúsculas
    matches = [word for word in signos if word.lower().startswith(query)]  # Compara en minúsculas
    return jsonify(matches)

if __name__ == "__main__":
    app.run(debug=True)

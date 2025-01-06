#!/usr/bin/env python
from flask import Flask, request, jsonify, render_template, redirect, url_for, session
from collections import OrderedDict
from significados import *
app = Flask(__name__)

"""
sol
luna
ascendente
planetas
quiron
casas
"""

@app.route("/") 
def index():
    return render_template("index.html")

@app.route("/autocompleteSigno", methods=["GET"])
def autocompleteSigno():
    query = request.args.get("q", "").lower()  # Convierte la consulta a minúsculas
    matches = [word for word in signos if word.lower().startswith(query)]  # Compara en minúsculas
    return jsonify(matches)

@app.route("/autocompleteCasa", methods=["GET"])
def autocompleteCasa():
    query = request.args.get("q", "").lower()  # Convierte la consulta a minúsculas
    matches = [word for word in casas if word.lower().startswith(query)]  # Compara en minúsculas
    return jsonify(matches)
    
# Necesitamos una clave secreta para usar la sesión en Flask
app.secret_key = 'your_secret_key_here'  # Cambia esto por una clave secreta en producción

# Ruta para procesar el formulario y mostrar los resultados
@app.route('/result', methods=['POST'])
def result():
    # Obtener los valores enviados desde el formulario
    input_values = request.form.to_dict()  # Convierte los datos de la solicitud en un diccionario
    #print("Datos recibidos en /result:", input_values)  # Verifica los datos recibidos

    # Almacenar los valores en la sesión
    session['input_values'] = input_values
    #print("Datos almacenados en sesión:", session.get('input_values'))  # Verifica que los datos se han almacenado correctamente

    # Redirigir al usuario a la página de resultados
    return redirect(url_for('show_result'))

@app.route('/result_page')
def show_result():
    # Recuperar los datos desde la sesión
    input_values = session.get('input_values', None)

    print("Datos recuperados de la sesión:", input_values)  # Verifica que los datos están siendo recuperados

    sol = input_values['autocomplete-input-1']
    luna = input_values['autocomplete-input-2']
    ascendente = input_values['autocomplete-input-3']
    mercurio = input_values['autocomplete-input-4']
    venus = input_values['autocomplete-input-5']
    marte = input_values['autocomplete-input-6']
    jupiter = input_values['autocomplete-input-7']
    saturno = input_values['autocomplete-input-8']
    urano = input_values['autocomplete-input-9']
    neptuno = input_values['autocomplete-input-10']
    pluton = input_values['autocomplete-input-11']
    quiron = input_values['autocomplete-input-12']



    context = {
        'solGeneral': soles["general"],
        'sol': sol,
        'solElemento': soles[sol][0],
        'viaje': soles[sol][1],
        'talentos': soles[sol][2],
        'retos':soles[sol][3],
        'luna': luna,
        'ascendente': ascendente,
        'mercurio' : mercurio,
        'venus': venus,
        'marte': marte,
        'jupiter': jupiter,
        'saturno': saturno,
        'urano': urano,
        'neptuno': neptuno,
        'pluton': pluton,
        'quiron': quiron
    }

    # Pasar los datos a la plantilla
    return render_template('result.html', **context)

if __name__ == "__main__":
    app.run(debug=True)


"""
    <ul>
        {% for input_id, value in input_values.items() %}
            <li><strong>{{ input_id }}:</strong> {{ value }}</li>
        {% endfor %} marina
    </ul>
"""
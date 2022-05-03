from flask import Flask, render_template, url_for #Importamos las librerias a ser usadas
import requests

hacena = Flask(__name__)  #Creabamos el objetoi hacena


@hacena.route("/")     #Llamabamos al metodo route y le pasamos el argumento slug o url
def inicio(): #Creamos la funcion inicio
    return render_template('inicio.html')
                #Retornamos la renderizacion de un documento

@hacena.route("/trabajana")
def trabajana():
    return render_template('trabajana.html')

@hacena.route("/contratana")
def contratana():
    return render_template('contratana.html')

@hacena.route("/aprendena")
def aprendena():
    return render_template('aprendena.html')

@hacena.route("/ensenana")
def ensenana():
    return render_template('ensenana.html')

@hacena.route("/ingresana")
def ingresana():
    return render_template('ingresana.html')

@hacena.route("/registratena")
def registratena():
    return render_template('registratena.html')

@hacena.route("/informatena")
def informatena():
    return render_template('informatena.html')

@hacena.route("/contratana_menu")
def contratana_menu():
    return render_template('contratana_menu.html')

@hacena.route("/contactana")
def contactana():
    return render_template('contactana.html')

@hacena.route("/publicana")
def publicana():
    return render_template('publicana.html')

@hacena.route("/profile_card2")
def profile_card2():
    return render_template('profile_card2.html')

if __name__ == "__main__":
    app.run(debug=True)
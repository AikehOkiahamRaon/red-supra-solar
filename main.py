from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Bienvenido a la Red Solar de Enlazamiento del Ser"})

@app.route('/curso')
def curso():
    return jsonify({"curso": "Contenido del curso de Activación del Guardián Brújula en la Red"})

@app.route('/biblioteca')
def biblioteca():
    return jsonify({"biblioteca": "Accede a libros, cursos, audios y transmisiones"})

@app.route('/donar')
def donar():
    return jsonify({"donaciones": "Opción para realizar una donación consciente"})

@app.route('/tienda')
def tienda():
    return jsonify({"tienda": "Adquiere libros, cursos y sesiones"})

@app.route('/sobre')
def sobre():
    return jsonify({"sobre": "Conoce a la creadora y la energía de la Red Solar"})

if __name__ == '__main__':
    app.run()

from flask import Flask
#clase importada

app = Flask(__name__)
#iniciamos la app

#rutas y vistas
@app.route('/')
#vista llamada index
def index():
    return "<h1>hola mundo_cuatro</h1>"

#comprobamos si estamos en el archivo main
if __name__=='__main__':
    app.run(debug=True, port=5000)
#entonces vamos a iniciar 
#agregamos debug=True para que el SERVER se actualice

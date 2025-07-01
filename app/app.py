from flask import Flask
#clase importada

app = Flask(__name__)
#iniciamos la app

#rutas y vistas
@app.route('/')
#vista llamada index
def index():
    return "hola mundo"

#comprobamos si estamos en el archivo main
if __name__=='__main__':
    app.run()
#entonces vamos a iniciar 
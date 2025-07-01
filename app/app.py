from flask import Flask, render_template
#clase importada

app = Flask(__name__)
#iniciamos la app

#rutas y vistas
@app.route('/')
#vista llamada index
def index():
#    return "<h1>hola mundo_cuatro</h1>"
    data={
        'titulo':'Index',
        'bienvenida':'Saludos'
    }
    return render_template('index.html', data=data)

#comprobamos si estamos en el archivo main
if __name__=='__main__':
    app.run(debug=True, port=5000)
#entonces vamos a iniciar 
#agregamos debug=True para que el SERVER se actualice

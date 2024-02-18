from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') #Ruta Raiz
def index ():
    #return "<h1>Hola Mundo!</h1>"
    cursos = ['PHP','Python','Java','Kotlin','Dart','JavaScript']
    data = {
        'titulo' : 'Index',
        'bienvenida' : '!Saludos!',
        'cursos' : cursos,
        'numero_cursos' : len(cursos)
    }
    return render_template('index.html', data = data)

if __name__ == '__main__':
    app.run(debug=True, port = 5000)

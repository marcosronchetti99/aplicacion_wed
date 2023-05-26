from Flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
    #return'bunas tardes'
   cursos= {'php', 'python', 'java', 'javascript'}
   data={
       'titulo':'index1',
       'bienvenida': 'saludos',
       'cursos':'cursos',
       'numero_cursos' : len(cursos)
   }
   return render_template('index.html',data=data)

if __name__=='__main__':
    app.run(debug=True, port=5000)
    
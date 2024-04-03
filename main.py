# Import
from flask import Flask, render_template,request, redirect
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///portfolio.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Comentario(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), nullable=False)
    comentario = db.Column(db.Text, nullable=False)
    def __repr__(self):
        return f"comentario {self.id}"

# Página de contenidos en ejecución
@app.route('/')
def index():
    return render_template('index.html')


# Habilidades dinámicas
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_discord = request.form.get('button_discord')
    button_html = request.form.get('button_html')
    button_db = request.form.get('button_db')

    if button_python == "SHOW PROJECT":
        return render_template('index.html', button_python=button_python)
    elif button_discord == "SHOW PROJECT":
        return render_template('index.html', button_discord=button_discord)
    elif button_html == "SHOW PROJECT":
        return render_template('index.html', button_html=button_html)
    elif button_db == "SHOW PROJECT":
        coment=Comentario.query.all()
        for i in coment:
         print(i.comentario,i.email)
        return render_template('index.html', button_db=button_db)
    else:
        return process_playback()


@app.route('/', methods=['POST'])
def process_playback():
    if request.method == 'POST':
        email = request.form.get('email')
        text = request.form.get('text')
        button = request.form.get('form_button')

        comentario = Comentario(email=email, comentario=text)
        db.session.add(comentario)
        db.session.commit()

    return render_template('index.html', button=button)

if __name__ == "__main__":
    app.run(debug=True)

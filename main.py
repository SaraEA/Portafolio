# Import
from flask import Flask, render_template,request, redirect



app = Flask(__name__)

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
        return render_template('index.html', button_db=button_db)


@app.route('/', methods=['POST'])
def process_playback():
    if request.method == 'POST':
        email = request.form['email']
        text = request.form['text']
        button = request.form.get('form_button')
    return render_template('index.html', button=button)

if __name__ == "__main__":
    app.run(debug=True)

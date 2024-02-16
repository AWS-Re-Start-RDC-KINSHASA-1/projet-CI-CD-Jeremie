from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/login', methods=['POST'])
def login():
    # Récupérer les données du formulaire
    username = request.form['username']
    password = request.form['password']
    # Vérifier les informations de connexion
    if username == 'kams' and password == '123456':
        # Redirection vers la page souhaitée
        return redirect(url_for('dashboard'))
    else:
        # Redirection vers une page d'erreur
        return redirect(url_for('error'))
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/error')
def error():
    return render_template('error.html')
if __name__ == '__main__':
    app.run()
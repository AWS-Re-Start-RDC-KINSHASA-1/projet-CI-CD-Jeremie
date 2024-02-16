from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/success')
def success():
    data = {
        'message': 'OK',
        'http_code': 200
    }
    return jsonify(data)
@app.route('/login', methods=['POST'])
def login():
    # Récupérer les données du formulaire
    username = request.form['username']
    password = request.form['password']
    # Vérifier les informations de connexion
    if username == 'kams' and password == '123456':
        # Redirection vers la page souhaitée
        return render_template('dashboard.html')
    else:
        # Redirection vers une page d'erreur
        return render_template('error.html')
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/error')
def error():
    return render_template('error.html')
if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5000')
from flask import Flask, render_template, redirect, url_for, session, request
import sqlite3
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Clé secrète sécurisée générée dynamiquement

# Fonction pour vérifier si l'utilisateur est authentifié
def est_authentifie():
    return session.get('authentifie')

# Fonction utilitaire pour se connecter à la base de données
def get_db_connection(db_name):
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row  # Permet d'accéder aux colonnes par nom
    return conn

@app.route('/')
def hello_world():
    return render_template('hello.html')  # Un seul return

@app.route('/lecture')
def lecture():
    if not est_authentifie():
        return redirect(url_for('authentification'))
    return "<h2>Bravo, vous êtes authentifié</h2>"

@app.route('/authentification', methods=['GET', 'POST'])
def authentification():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if username == 'admin' and password == 'password':  # À remplacer par une vérification sécurisée
            session['authentifie'] = True
            return redirect(url_for('lecture'))
        else:
            return render_template('formulaire_authentification.html', error=True)

    return render_template('formulaire_authentification.html', error=False)

@app.route('/fiche_client/<int:post_id>')
def Readfiche(post_id):
    conn = get_db_connection('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients WHERE id = ?', (post_id,))
    data = cursor.fetchall()
    conn.close()
    return render_template('read_data.html', data=data)

@app.route('/consultation/')
def ReadBDD():
    conn = get_db_connection('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients;')
    data = cursor.fetchall()
    conn.close()
    return render_template('read_data.html', data=data)

@app.route('/consultation_livre/')
def ReadBDDlivre():
    conn = get_db_connection('databaselivre.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livres;')
    data = cursor.fetchall()
    conn.close()
    return render_template('read_data2.html', data=data)

@app.route('/enregistrer_client', methods=['GET'])
def formulaire_client():
    return render_template('formulaire.html')

@app.route('/enregistrer_client', methods=['POST'])
def enregistrer_client():
    nom = request.form.get('nom')
    prenom = request.form.get('prenom')

    if not nom or not prenom:
        return "Nom et prénom sont obligatoires", 400

    try:
        conn = get_db_connection('database.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO clients (created, nom, prenom, adresse) VALUES (?, ?, ?, ?)',
                       (1002938, nom, prenom, "ICI"))
        conn.commit()
    except sqlite3.Error as e:
        return f"Erreur de base de données : {e}", 500
    finally:
        conn.close()

    return redirect(url_for('ReadBDD'))  # Redirection correcte

if __name__ == "__main__":
    app.run(debug=True)

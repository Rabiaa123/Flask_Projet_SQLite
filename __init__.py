from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'  # Clé secrète pour les sessions

# Fonction pour vérifier si l'utilisateur est authentifié
def est_authentifie():
    return session.get('authentifie')

# Page d'accueil
@app.route('/')
def accueil():
    return render_template('hello.html')

# Authentification
@app.route('/authentification', methods=['GET', 'POST'])
def authentification():
    if request.method == 'POST':
        # Vérifier les identifiants
        if request.form['username'] == 'admin' and request.form['password'] == 'password':  # À remplacer par une vérification en base de données
            session['authentifie'] = True
            return redirect(url_for('lecture'))
        else:
            return render_template('formulaire_authentification.html', error=True)
    return render_template('formulaire_authentification.html', error=False)

# Page de lecture (réservée aux utilisateurs authentifiés)
@app.route('/lecture')
def lecture():
    if not est_authentifie():
        return redirect(url_for('authentification'))
    return "<h2>Bravo, vous êtes authentifié</h2>"

# Consultation des clients
@app.route('/consultation/')
def consultation_clients():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clients;')
    data = cursor.fetchall()
    conn.close()
    return render_template('read_data.html', data=data)

# Consultation des livres
@app.route('/consultation_livres/')
def consultation_livres():
    conn = sqlite3.connect('bibliotheque.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livres;')
    data = cursor.fetchall()
    conn.close()
    return render_template('read_data2.html', data=data)

# Fiche d'un livre
@app.route('/fiche_livre/<int:livre_id>')
def fiche_livre(livre_id):
    conn = sqlite3.connect('bibliotheque.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livres WHERE id = ?', (livre_id,))
    data = cursor.fetchone()
    conn.close()
    return render_template('fiche_livre.html', livre=data)

# Formulaire pour enregistrer un livre
@app.route('/enregistrer_livre', methods=['GET'])
def formulaire_livre():
    return render_template('formulaire2.html')

# Enregistrer un livre
@app.route('/enregistrer_livre', methods=['POST'])
def enregistrer_livre():
    titre = request.form['titre']
    auteur = request.form['auteur']
    isbn = request.form['isbn']
    genre = request.form['genre']
    annee_publication = request.form['annee_publication']

    # Connexion à la base de données
    conn = sqlite3.connect('bibliotheque.db')
    cursor = conn.cursor()

    # Exécution de la requête SQL pour insérer un nouveau livre
    cursor.execute('''
        INSERT INTO livres (titre, auteur, isbn, genre, annee_publication)
        VALUES (?, ?, ?, ?, ?)
    ''', (titre, auteur, isbn, genre, annee_publication))

    # Valider la transaction
    conn.commit()
    conn.close()

    # Rediriger vers la liste des livres
    return redirect(url_for('consultation_livres'))

if __name__ == "__main__":
    app.run(debug=True)

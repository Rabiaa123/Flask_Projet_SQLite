import sqlite3

# Connexion à la base de données
connection = sqlite3.connect('bibliotheque.db')

# Chargement du script SQL pour créer les tables
with open('schema2.sql', 'r') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# Insertion des livres dans la table "livres"
cur.execute("INSERT INTO livres (titre, auteur, isbn, genre, annee_publication) VALUES (?, ?, ?, ?, ?)",
            ('Emilie', 'Victor', '1234567890', 'Roman', 2024))
cur.execute("INSERT INTO livres (titre, auteur, isbn, genre, annee_publication) VALUES (?, ?, ?, ?, ?)",
            ('Didier', 'Laurent', '0987654321', 'Essai', 2023))

# Insertion des stocks associés aux livres
cur.execute("INSERT INTO stocks (livre_id, quantite) VALUES (?, ?)", (1, 10))
cur.execute("INSERT INTO stocks (livre_id, quantite) VALUES (?, ?)", (2, 5))

# Validation des modifications et fermeture de la connexion
connection.commit()
connection.close()

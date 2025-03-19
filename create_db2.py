import sqlite3

# Connexion à la base de données (elle sera créée si elle n'existe pas)
connection = sqlite3.connect('bibliotheque.db')

# Exécution du schéma SQL pour créer les tables
with open('schema2.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# Insertion des utilisateurs de démonstration
cur.execute("INSERT INTO utilisateurs (nom, prenom, email, mot_de_passe, role) VALUES (?, ?, ?, ?, ?)",
            ('DUPONT', 'Emilie', 'emilie.dupont@example.com', 'password123', 'utilisateur'))
cur.execute("INSERT INTO utilisateurs (nom, prenom, email, mot_de_passe, role) VALUES (?, ?, ?, ?, ?)",
            ('LEROUX', 'Lucas', 'lucas.leroux@example.com', 'password123', 'admin'))
cur.execute("INSERT INTO utilisateurs (nom, prenom, email, mot_de_passe, role) VALUES (?, ?, ?, ?, ?)",
            ('MARTIN', 'Amandine', 'amandine.martin@example.com', 'password123', 'utilisateur'))

# Insertion des livres de démonstration
cur.execute("INSERT INTO livres (titre, auteur, isbn, genre, annee_publication) VALUES (?, ?, ?, ?, ?)",
            ('Le Petit Prince', 'Antoine de Saint-Exupéry', '9782070408504', 'Littérature', 1943))
cur.execute("INSERT INTO livres (titre, auteur, isbn, genre, annee_publication) VALUES (?, ?, ?, ?, ?)",
            ('1984', 'George Orwell', '9782070368228', 'Science-Fiction', 1949))
cur.execute("INSERT INTO livres (titre, auteur, isbn, genre, annee_publication) VALUES (?, ?, ?, ?, ?)",
            ('Le Seigneur des Anneaux', 'J.R.R. Tolkien', '9782266282362', 'Fantasy', 1954))

# Insertion des stocks de démonstration
cur.execute("INSERT INTO stocks (livre_id, quantite) VALUES (?, ?)", (1, 5))  # 5 exemplaires du Petit Prince
cur.execute("INSERT INTO stocks (livre_id, quantite) VALUES (?, ?)", (2, 3))  # 3 exemplaires de 1984
cur.execute("INSERT INTO stocks (livre_id, quantite) VALUES (?, ?)", (3, 7))  # 7 exemplaires du Seigneur des Anneaux

# Insertion des emprunts de démonstration
cur.execute("INSERT INTO emprunts (utilisateur_id, livre_id, date_emprunt, date_retour_prevue) VALUES (?, ?, ?, ?)",
            (1, 1, '2023-10-01', '2023-10-15'))  # Emilie emprunte Le Petit Prince
cur.execute("INSERT INTO emprunts (utilisateur_id, livre_id, date_emprunt, date_retour_prevue) VALUES (?, ?, ?, ?)",
            (2, 2, '2023-10-05', '2023-10-20'))  # Lucas emprunte 1984

# Validation des modifications
connection.commit()

# Fermeture de la connexion à la base de données
connection.close()

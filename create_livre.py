import sqlite3

try:
    # Connexion à la base de données
    connection = sqlite3.connect('databaselivre.db')

    # Exécution du script SQL pour créer la table
    with open('schemalivre.sql') as f:
        connection.executescript(f.read())

    # Création d'un curseur
    cur = connection.cursor()

    # Insertion des données
    cur.execute("INSERT INTO Livres (ID_livre, Titre, Auteur, Annee_publication, Quantite) VALUES (?, ?, ?, ?, ?)", (1, 'JAVA', 'Victor', 2024, 10))
    cur.execute("INSERT INTO Livres (ID_livre, Titre, Auteur, Annee_publication, Quantite) VALUES (?, ?, ?, ?, ?)", (2, 'HTML', 'Laurent', 2023, 5))
    cur.execute("INSERT INTO Livres (ID_livre, Titre, Auteur, Annee_publication, Quantite) VALUES (?, ?, ?, ?, ?)", (3, 'SQL', 'Nathalie', 2025, 20))
    cur.execute("INSERT INTO Livres (ID_livre, Titre, Auteur, Annee_publication, Quantite) VALUES (?, ?, ?, ?, ?)", (4, 'PYTHON', 'Rabiaa', 2020, 15))

    # Validation des changements
    connection.commit()

except sqlite3.Error as e:
    print(f"Une erreur SQLite s'est produite : {e}")

finally:
    # Fermeture de la connexion
    if connection:
        connection.close()

import sqlite3

try:
    # Connexion à la base de données
    connection = sqlite3.connect('databaselivre.db')
    connection.execute("PRAGMA foreign_keys = ON;")  # Activer les clés étrangères

    # Exécution du script SQL
    with open('schemalivre.sql') as f:
        connection.executescript(f.read())

    print("Tables créées avec succès.")

except sqlite3.Error as e:
    print(f"Une erreur SQLite s'est produite : {e}")

finally:
    # Fermeture de la connexion
    if connection:
        connection.close()

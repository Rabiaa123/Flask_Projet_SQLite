import sqlite3

connection = sqlite3.connect('bibliotheque.db')

with open('schemalivre.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO Livres (ID_livre, Titre, Auteur, Annee_publication, Quantite) VALUES (?, ?, ?, ?, ?)",(1, 'JAVA', 'Victor', 2024, 10))
cur.execute("INSERT INTO Livres (ID_livre, Titre, Auteur, Annee_publication, Quantite) VALUES (?, ?, ?, ?, ?)",(2, 'HTML', 'Laurent', 2023, 5))
cur.execute("INSERT INTO Livres (ID_livre, Titre, Auteur, Annee_publication, Quantite) VALUES (?, ?, ?, ?, ?)",(3, 'SQL', 'Nathalie', 2025, 20))
cur.execute("INSERT INTO Livres (ID_livre, Titre, Auteur, Annee_publication, Quantite) VALUES (?, ?, ?, ?, ?)",(4, 'PYTHON', 'Rabiaa', 2020, 15))

connection.commit()
connection.close()

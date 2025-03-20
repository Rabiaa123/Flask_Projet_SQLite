import sqlite3

# Connexion à la base de données
connection = sqlite3.connect('bibliotheque.db')

# Chargement du script SQL pour créer les tables
with open('schema2.sql', 'r') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# Liste des livres à insérer
livres = [
    (1, 'Le Petit Prince', 'Antoine de Saint-Exupéry', 1943, 15),
    (2, '1984', 'George Orwell', 1949, 8),
    (3, "L'Étranger", 'Albert Camus', 1942, 12),
    (4, 'Harry Potter à l\'école des sorciers', 'J.K. Rowling', 1997, 29),
    (5, 'Les Misérables', 'Victor Hugo', 1862, 5),
    (6, 'La Peste', 'Albert Camus', 1947, 10)
]

# Insertion des livres dans la table Livres
for livre in livres:
    cur.execute("""
        INSERT INTO Livres (ID_livre, Titre, Auteur, Annee_publication, Quantite)
        VALUES (?, ?, ?, ?, ?)
    """, livre)

# Liste des stocks à insérer
stocks = [
    (1, 10),
    (2, 5),
    (3, 19),
    (4, 2),
    (5, 16),
    (6, 10)
]

# Insertion des stocks associés aux livres
for stock in stocks:
    cur.execute(
        INSERT INTO stocks (ID_livre, Quantite)
        VALUES (?, ?)
    , stock)

# Validation des modifications et fermeture de la connexion
connection.commit()
connection.close()

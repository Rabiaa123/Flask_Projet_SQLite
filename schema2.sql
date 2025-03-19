-- Suppression des tables si elles existent déjà
DROP TABLE IF EXISTS utilisateurs;
DROP TABLE IF EXISTS livres;
DROP TABLE IF EXISTS emprunts;
DROP TABLE IF EXISTS stocks;

-- Table pour gérer les utilisateurs
CREATE TABLE utilisateurs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    nom TEXT NOT NULL,
    prenom TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    mot_de_passe TEXT NOT NULL,
    role TEXT NOT NULL DEFAULT 'utilisateur' -- 'utilisateur' ou 'admin'
);

-- Table pour gérer les livres
CREATE TABLE Livres (
    titre TEXT NOT NULL,
    auteur TEXT NOT NULL,
    isbn TEXT NOT NULL,
    genre TEXT,
    annee_publication INTEGER
);

-- Table pour gérer les emprunts
CREATE TABLE emprunts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    utilisateur_id INTEGER NOT NULL,
    livre_id INTEGER NOT NULL,
    date_emprunt DATE NOT NULL,
    date_retour_prevue DATE NOT NULL,
    date_retour_effective DATE,
    FOREIGN KEY (utilisateur_id) REFERENCES utilisateurs(id),
    FOREIGN KEY (livre_id) REFERENCES livres(id)
);

-- Table pour gérer les stocks
CREATE TABLE stocks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    livre_id INTEGER NOT NULL,
    quantite INTEGER NOT NULL DEFAULT 0,
    FOREIGN KEY (livre_id) REFERENCES livres(id)
);

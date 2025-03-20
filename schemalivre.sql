-- Activer le support des clés étrangères
PRAGMA foreign_keys = ON;

-- Créer la table Livres
CREATE TABLE IF NOT EXISTS Livres (
    ID_livre INTEGER PRIMARY KEY,
    Titre TEXT NOT NULL,
    Auteur TEXT NOT NULL,
    Annee_publication INTEGER,
    Quantite INTEGER
);

-- Créer la table Utilisateurs
CREATE TABLE IF NOT EXISTS Utilisateurs (
    ID_utilisateur INTEGER PRIMARY KEY,
    Nom TEXT NOT NULL,
    Prenom TEXT NOT NULL,
    Email TEXT NOT NULL UNIQUE,
    Date_inscription TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Créer la table Emprunts
CREATE TABLE IF NOT EXISTS Emprunts (
    ID_emprunt INTEGER PRIMARY KEY,
    ID_utilisateur INTEGER,
    ID_livre INTEGER,
    Date_emprunt DATE,
    Date_retour_prevue DATE,
    Date_retour_effective DATE,
    FOREIGN KEY (ID_utilisateur) REFERENCES Utilisateurs(ID_utilisateur) ON DELETE CASCADE,
    FOREIGN KEY (ID_livre) REFERENCES Livres(ID_livre) ON DELETE CASCADE
);

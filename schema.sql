CREATE DATABASE gestion_stock;

USE gestion_stock;

CREATE TABLE categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom_categorie VARCHAR(100) NOT NULL UNIQUE
);

CREATE TABLE produits (
    id INT AUTO_INCREMENT PRIMARY KEY,
    designation VARCHAR(150) NOT NULL,
    prix DECIMAL(10,2) NOT NULL CHECK (prix >= 0),
    stock INT NOT NULL DEFAULT 0 CHECK (stock >= 0),
    id_categorie INT NOT NULL,
    
    CONSTRAINT fk_produit_categorie
        FOREIGN KEY (id_categorie)
        REFERENCES categories(id)
        ON DELETE RESTRICT
);

CREATE TABLE mouvements (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_produit INT NOT NULL,
    type_mouvement ENUM('ENTREE', 'SORTIE') NOT NULL,
    quantite INT NOT NULL CHECK (quantite > 0),
    date_mouvement DATETIME DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_mouvement_produit
        FOREIGN KEY (id_produit)
        REFERENCES produits(id)
        ON DELETE CASCADE
);

CREATE TABLE utilisateurs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    prenom VARCHAR(50) NOT NULL,
    nom VARCHAR(50) NOT NULL,
    email VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    role ENUM('admin', 'user') DEFAULT 'user'
);

-- Affichage produit et de leur catégorie
SELECT 
    p.designation,
    p.prix,
    p.stock,
    p.en_rupture,
    c.nom_categorie
FROM produits p
JOIN categories c ON p.id_categorie = c.id

-- Affichage historique
SELECT
    p.designation,
    m.quantite,
    m.type_mouvement,
    m.date_mouvement
FROM mouvements m
JOIN produits p ON m.id_produit = p.id
ORDER BY m.date_mouvement DESC;
    
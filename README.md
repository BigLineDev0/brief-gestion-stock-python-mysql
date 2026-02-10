# 📦 Gestion de Stock – Python & MySQL

## 📝 Description
Application console permettant de gérer le stock de matériel d’une structure solidaire.  
Elle assure le suivi des produits, des catégories et l’historique des entrées et sorties de stock.

---

## ⚙️ Fonctionnalités
- Ajout et affichage des catégories  
- Ajout et affichage des produits  
- Gestion du stock (entrée / sortie)  
- Historique des mouvements  
- Alerte stock faible (< 5)  
- Validation des données  

---

## 🗄️ Base de données
- **categories** (`id`, `nom_categorie`)
- **produits** (`id`, `designation`, `prix`, `stock`, `id_categorie`)
- **mouvements** (`id`, `id_produit`, `type_mouvement`, `quantite`, `date_mouvement`)

### Règles importantes
- La désignation d’un produit est **unique**
- Le stock ne peut pas être négatif
- Toute modification du stock est historisée

---

## 🛠️ Technologies
- Python 3
- MySQL
- mysql-connector-python

---
### 1. Cloner le projet
## 🚀 Installation et exécution

- git clone <url-du-repo>
- cd gestion-stock

### 2. Création environement virtuel et activation

- python3 -m venv .env

- source venv .env/bin/activate

### 3. Installer les dépendances
- pip install mysql-connector-python

### 4. Configurer la base de données

- Créer la base MySQL

- Importer le script SQL (tables + contraintes)

- Mettre à jour les paramètres de connexion dans db.py

### 5. Lancement
- python main.py
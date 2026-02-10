from db import get_connection
from model.categories import saisir_choix, afficher_categorie, ajouter_categorie, supprimer_categorie
from model.produits import afficher_produits, ajouter_produit
from model.mouvements import entree_stock, sortie_stock

# Geston Catégorie
def gestion_categorie():
    print('\n','-' * 40)
    print("1. Ajouter une catégorie")
    print("2. Afficher les catégories")
    print("3. Supprimer une catégorie")
    print("0. Accueil")
    print('-' * 40)

    choix = saisir_choix(['1', '2', '3', '0'])
    match choix:
        case '1':
            ajouter_categorie()

        case '2':
            afficher_categorie()

        case '3':
            supprimer_categorie()
    
        case '0':
            afficher_produits()

# Gestion des produits
def gestion_produit():

    afficher_produits()

    print('\n','-' * 40)
    print("1. Ajouter un produit")
    print("2. Modifier un produit")
    print("3. Supprimer un produit")
    print("0. Accueil")
    print('-' * 40)

    choix = saisir_choix(['1', '2', '3', '0'])
    match choix:
        case '1':
            ajouter_produit()

        case '2':
            print("Non disponible")

        case '3':
            print("Non disponible")
    
        case '0':
            afficher_produits()

# Effectuer un mouvement
def effectuer_mouvement():
    print('\n','-' * 40)
    print("1. Entrée stock")
    print("2. Sortie stock")
    print("0. Accueil")
    print('-' * 40)

    choix = saisir_choix(['1', '2', '0'])
    match choix:
        case '1':
            entree_stock()

        case '2':
            sortie_stock()
    
        case '0':
            afficher_produits()

# Afficher l'historique des mouvements
def afficher_historiques():
    conn = get_connection()
    if conn is None:
        return

    try:
        cursor = conn.cursor(dictionary=True)
        query = """
        SELECT
            p.designation,
            m.quantite,
            m.type_mouvement,
            m.date_mouvement
        FROM mouvements m
        JOIN produits p ON m.id_produit = p.id
        ORDER BY m.date_mouvement DESC;  
        """
        cursor.execute(query)
        historiques = cursor.fetchall()

        if not historiques:
            print("\nAucune historique.")
            return []
        
        print("\nListe des historiques :")
        for i, historique in enumerate(historiques, start=1):

            print(f"{i}. Produit: {historique['designation']} - Quantité: {historique['quantite']} - Type: {historique['type_mouvement']} - Date: ({historique['date_mouvement']})")

    except Exception as e:
        print("Erreur lors de recuperation de la liste des produits", e)
    finally:
        cursor.close()
        conn.close()

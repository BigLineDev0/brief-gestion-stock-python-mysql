from db import get_connection
from model.produits import afficher_produits

# Ajouter un stock
def entree_stock():
    conn = get_connection()
    if conn is None:
        return
    
    cursor = conn.cursor(dictionary=True)

    afficher_produits()

    id_produit = input("\nChoisissez ID du produit : ")

    while True:
        try:
            quantite = int(input("Quantité : "))
        
            if quantite <= 0:
                print("ERREUR : Veuillez entrer un nombre positif")
            else:
                break

        except ValueError:
            print("Quantité invalide. Veuillez réessayer.")

    try:

        # Stock actuel
        cursor.execute("SELECT * FROM produits WHERE id = %s", (id_produit,))
        produit = cursor.fetchone()

        if not produit:
            print("Produit inexistant")
            return

        # Historique
        cursor.execute("""
            INSERT INTO mouvements (id_produit, type_mouvement, quantite)
            VALUES (%s, 'ENTREE', %s)
        """, (id_produit, quantite))

        nouveau_stock = produit['stock'] + quantite

        # Mise à jour produit
        cursor.execute("""
            UPDATE produits
            SET stock = %s
            WHERE id = %s
        """, (nouveau_stock, id_produit,))

        conn.commit()
        print("Entrée de stock effectuée")

    except Exception as e:
        # conn.rollback()
        print("Erreur :", e)

    finally:
        cursor.close()
        conn.close()

# Effectuer une sortie de stock
def sortie_stock():
    conn = get_connection()
    if conn is None:
        return
    
    cursor = conn.cursor(dictionary=True)

    afficher_produits()

    id_produit = input("\nChoisissez ID du produit : ")

    while True:
        try:
            quantite = int(input("Quantité : "))
        
            if quantite <= 0:
                print("ERREUR : Veuillez entrer un nombre positif")
            else:
                break

        except ValueError:
            print("Quantité invalide. Veuillez réessayer.")

    try:

        # Stock actuel
        cursor.execute("SELECT * FROM produits WHERE id = %s", (id_produit,))
        produit = cursor.fetchone()

        if not produit:
            print("Produit inexistant")
            return
        
        if produit['stock'] < quantite:
            print('Stock insuffisant.')
            return

        # Historique
        cursor.execute("""
            INSERT INTO mouvements (id_produit, type_mouvement, quantite)
            VALUES (%s, 'SORTIE', %s)
        """, (id_produit, quantite))

        nouveau_stock = produit['stock'] - quantite

        # Mise à jour produit
        cursor.execute("""
            UPDATE produits
            SET stock = %s
            WHERE id = %s
        """, (nouveau_stock, id_produit,))

        conn.commit()
        print("Sortie de stock effectuée")

    except Exception as e:
        # conn.rollback()
        print("Erreur :", e)

    finally:
        cursor.close()
        conn.close()

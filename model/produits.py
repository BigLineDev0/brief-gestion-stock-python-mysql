from db import get_connection
from model.categories import afficher_categorie
# Valider la designation pour qu'il soit unique
def designation_existe(cursor, designation):
    cursor.execute(
        "SELECT id FROM produits WHERE designation = %s",
        (designation,)
    )
    return cursor.fetchone() is not None 

# Ajouter un produit
def ajouter_produit():
    conn = get_connection()
    if conn is None:
        return

    while True:
        designation = input("Désignation du produit : ").strip()

        if len(designation) < 3:
            print("La désignation doit contenir au moins 3 caractères")
            continue

    
        if designation.isdigit():
            print("La désignation ne peut pas contenir uniquement des chiffres")
            continue

        designation = designation.title()  

        break

    while True:
        try:
            prix = float(input("Prix : "))
        
            if prix < 0:
                print("ERREUR : Veuillez entrer un nombre positif")
            else:
                break

        except ValueError:
            print("Prix invalide. Veuillez réessayer.")

    while True:
        
        afficher_categorie()

        id_categorie = input("Choisissez ID de la catégorie : ")

        if not id_categorie.isdigit():
            print("ID invalide")
            continue

        cursor = conn.cursor()
        cursor.execute(
            "SELECT id FROM categories WHERE id = %s",
            (id_categorie,)
        )

        if cursor.fetchone():
            break

        print("Catégorie inexistante")

    while True:
        try:
            stock = int(input("Stock : "))
        
            if stock < 0:
                print("ERREUR : Veuillez entrer un nombre positif")
            else:
                break

        except ValueError:
            print("Stock invalide. Veuillez réessayer.")

    try:
        cursor = conn.cursor()
        query = "INSERT INTO produits(designation, prix, stock, id_categorie) VALUES(%s, %s, %s, %s)"
        cursor.execute(query, (designation, prix, stock, id_categorie,))
        conn.commit()
        print("\nProduit ajouté avec succès.")

    except Exception as e:
        print("Erreur lors de l'ajout du produit", e)
    finally:
        cursor.close()
        conn.close()

# Afficher les produits
def afficher_produits():
    conn = get_connection()
    if conn is None:
        return

    try:
        cursor = conn.cursor(dictionary=True)
        query = """
        SELECT 
            p.id,
            p.designation,
            p.prix,
            p.stock,
            c.nom_categorie
        FROM produits p
        JOIN categories c ON p.id_categorie = c.id
        """
        cursor.execute(query)
        liste_produits = cursor.fetchall()

        if not liste_produits:
            print("\nAucun produit.")
            return []
        
        print("\nListe des produits :")
        for produit in liste_produits:
            if produit['stock'] < 5:
                etat = "En rupture"
            else:
                etat = "En stock"

            print(f"ID: {produit['id']}. Produit: {produit['designation']} - Prix: {produit['prix']}F - Stock: {produit['stock']} - Catégorie: {produit['nom_categorie']} | Etat: ({etat})")

    except Exception as e:
        print("Erreur lors de recuperation de la liste des produits", e)
    finally:
        cursor.close()
        conn.close()


# Afficher les produits en alerte
def alerte_produits():
    conn = get_connection()
    if conn is None:
        return

    try:
        cursor = conn.cursor(dictionary=True)
        query = """
        SELECT designation, prix, stock FROM produits WHERE stock < 5
        """
        cursor.execute(query)
        liste_produits = cursor.fetchall()

        if not liste_produits:
            print("\nAucun produit.")
            return []
        
        
        print("\nListe des produits en rupture :")
        for i, produit in enumerate(liste_produits, start=1):

            print(f"{i}. {produit['designation']} - {produit['prix']}F - {produit['stock']} - (stock faible)")

    except Exception as e:
        print("Erreur lors de recuperation de la liste des produits", e)
    finally:
        cursor.close()
        conn.close()

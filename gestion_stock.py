from db import get_connection

# Fonction pour saisir un choix
def saisir_choix(options):
    while True:
        choix = input("Choisissez une option : ").strip()
        if choix in options:
            return choix
        else:
            print("Option invalide.")

# Ajouter une catégorie
def ajouter_categorie():
    conn = get_connection()
    if conn is None:
        return

    while True:
        nom_categorie = input("Nom Catégorie (ex: électonique): ").strip()

        if len(nom_categorie) < 3:
            print("La catégorie doit contenir au moins 3 caractères")
            continue

        if nom_categorie.isdigit():
            print("La catégorie ne peut pas contenir uniquement des chiffres")
            continue
       
        break
       
    try:
        cursor = conn.cursor()
        query = "INSERT INTO categories(nom_categorie) VALUES(%s)"
        cursor.execute(query, (nom_categorie,))
        conn.commit()
        print("\nCatgorie ajoutée avec succès.")

    except Exception as e:
        print("Erreur lors de l'ajout de la catégorie", e)
    finally:
        cursor.close()
        conn.close()

# Afficher les catégories
def afficher_categorie():
    conn = get_connection()
    if conn is None:
        return

    try:
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM categories"
        cursor.execute(query)
        liste_categories = cursor.fetchall()

        if not liste_categories:
            print("\nAucune catégorie.")
            return []
        
        print("\nListe des catégories :")

        for cat in liste_categories:
            print(f"ID: {cat['id']} - {cat['nom_categorie']}")

    except Exception as e:
        print("Erreur lors de recuperation de la liste des catégories", e)
    finally:
        cursor.close()
        conn.close()

# Supprimer une catégorie
def supprimer_categorie():
    conn = get_connection()
    if conn is None:
        return

    try:
        cursor = conn.cursor(dictionary=True)

        afficher_categorie()
        id_categorie = input("\nChoisissez l'ID de la catégorie à supprimer : ")

        if not id_categorie.isdigit():
            print("ID invalide")
            return

        # Vérifier si la catégorie existe
        cursor.execute(
            "SELECT id FROM categories WHERE id = %s",
            (id_categorie,)
        )

        if not cursor.fetchone():
            print("Catégorie inexistante")
            return

        # Vérifier si des produits sont liés
        cursor.execute(
            "SELECT COUNT(*) AS total FROM produits WHERE id_categorie = %s",
            (id_categorie,)
        )
        result = cursor.fetchone()

        if result['total'] > 0:
            print("Impossible de supprimer : des produits sont associés à cette catégorie")
            return

        # Suppression
        cursor.execute(
            "DELETE FROM categories WHERE id = %s",
            (id_categorie,)
        )
        conn.commit()

        print("Catégorie supprimée avec succès")

    except Exception as e:
        print("Erreur lors de la suppression :", e)

    finally:
        cursor.close()
        conn.close()

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

# Effectuer un entrée de stock
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

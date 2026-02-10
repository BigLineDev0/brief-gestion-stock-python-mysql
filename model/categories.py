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
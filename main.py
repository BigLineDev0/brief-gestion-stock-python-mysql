from gestion_stock import ajouter_categorie, afficher_categorie, ajouter_produit, afficher_produits, effectuer_mouvement, alerte_produits, afficher_historiques, supprimer_categorie
# Fonction afficher le menu
def menu():

    print("\n-------- GESTION STOCK --------")
    print("1. Ajouter une catégorie")
    print("2. Afficher tous les catégories")
    print("3. Ajouter un produit")
    print("4. Afficher tous les produits")
    print("5. Mouvement de stock")
    print("6. Afficher les produits en alerte")
    print("7. Afficher l'historique")
    print("8. Supprimer une catégorie")
    print("0. Quitter")
    print("-" * 40)

# Démarage du programme
def main():
    while  True:
        menu()
        choix = input("\nChoisissez une option : ")
        match choix:
            case '1':
                ajouter_categorie()

            case '2':
                afficher_categorie()
            
            case '3':
                ajouter_produit()
            
            case '4':
                afficher_produits()
            
            case '5':
                effectuer_mouvement()

            case '6':
                alerte_produits()

            case '7':
                afficher_historiques()
            
            case '8':
                supprimer_categorie()

            case '0':
                print("Au revoir!")
                break 
            case _:
                print("\nOption invalide, veuillez réessayer.")
main()

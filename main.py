from gestion_stock import gestion_categorie, gestion_produit, effectuer_mouvement, afficher_historiques
from model.utilisateur import Ajouter_utilisateur,afficher_utilisateur
from model.produits import alerte_produits
# Fonction afficher le menu
def menu():

    print("\n----------- GESTION STOCK  BOUTIQUE PRO -------------")
    print("1. Gestion des catégories")
    print("2. Gestion des produits")
    print("3. Gestion du stock (entrée / sortie)")
    print("4. Alerte stock faible (< 5)")
    print("5. Historique des mouvements")
    print("6. Ajouter un utilisateur")
    print("7. Afficher les utilisateurs")
    print("0. Quitter")
    print("-" * 40)

# Démarage du programme
def main():
    while  True:
        menu()
        choix = input("\nChoisissez une option : ")
        match choix:
            case '1':
                gestion_categorie()

            case '2':
                gestion_produit()
            
            case '3':
                effectuer_mouvement()
            
            case '4':
                alerte_produits()
            
            case '5':
                afficher_historiques()
            
            case '6':
                Ajouter_utilisateur()

            case '0':
                print("Au revoir!")
                break 
            case _:
                print("\nOption invalide, veuillez réessayer.")


def auth():
    print('----------------Connexion----------------------')
    print()
    while True:
        email=input('veuillez saisir votre email ')
        mdp=input('veuillez saisir votre mot de pass ')
        u=afficher_utilisateur(email,mdp)
        if u != None:
            main()
        else:
            print('erreur de connexion')
auth()


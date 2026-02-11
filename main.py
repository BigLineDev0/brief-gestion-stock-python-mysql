from gestion_stock import gestion_categorie, gestion_produit, effectuer_mouvement, afficher_historiques
from model.utilisateur import Ajouter_utilisateur,utilisateur_connecter,mot_de_pass_hash,afficher_utilisateur
from model.produits import alerte_produits
from model.categories import afficher_categorie
from model.produits import afficher_produits
import bcrypt
# Fonction afficher le menu
def menu_admin():

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

def menu_user():
    print("\n----------- GESTION STOCK  BOUTIQUE PRO -------------")
    print("1. Afficher categorie")
    print("2. Afficher produits")
    print("3. Alerte stock faible (< 5)")
    print("4. Historique des mouvements")
    print("5. Afficher les utilisateurs")
    print("0. Quitter")
    print("-" * 40)

# Démarage du programme
def Admin():
    while  True:
        menu_admin()
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

            case '7':
                afficher_utilisateur()

            case '0':
                print("Au revoir!")
                break 
            case _:
                print("\nOption invalide, veuillez réessayer.")

def User():
    while  True:
        menu_user()
        choix = input("\nChoisissez une option : ")
        match choix:
            case '1':
                afficher_categorie()

            case '2':
                afficher_produits()
            
            case '3':
                alerte_produits()
            
            case '4':
                afficher_historiques()
            
            case '5':
                afficher_utilisateur()

            case '0':
                print("Au revoir!")
                break 
            case _:
                print("\nOption invalide, veuillez réessayer.")


def main():
    print('----------------Connexion----------------------')
    print()
    while True:
        while True:
            email=input('veuillez saisir votre email ')
            if "@" in email and "." in email and " " not in email:
                break
            else:
                print("Le mail saisi n'est pas valide")
        hash_mot_de_passe=mot_de_pass_hash(email)
        if hash_mot_de_passe == None:
            print("cette email n'existe pas")
        else:
            while True:
                mdp=input('veuillez saisir votre mot de pass ')
                if len(mdp) < 8:
                    print('Le mot de pass doit contenir au moins 8 caracteres')
                else:
                    break
            if bcrypt.checkpw(mdp.encode('utf-8'), hash_mot_de_passe.encode('utf-8')):
                u=utilisateur_connecter(email,hash_mot_de_passe)
                if u != None and u[0]=='user':
                    print(f'Bienvenue {u[2]} {u[1]}')
                    User()
                elif u != None and u[0]=='admin':
                    print(f'Bienvenue {u[2]} {u[1]}')
                    Admin()    
                else:
                    print('erreur de connexion')
            else:
                print("Mot de passe incorrect")
            
            
main()


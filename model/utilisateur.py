from db import get_connection
import bcrypt
def creer_utilisateur(nom,prenom,telephone,email,mot_de_pass,role):
    conn=get_connection()
    curseur=conn.cursor()
    try:
        sql='insert into utilisateurs(nom,prenom,telephone,email,mot_de_pass,role)values(%s,%s,%s,%s,%s,%s)'
        curseur.execute(sql,(nom,prenom,telephone,email,mot_de_pass,role))
        conn.commit()
        print('utilisateur ajouter avec succes')
    except Exception as e:
        print("erreur lors de l'enregistrement ",e)
    finally:
        curseur.close()
        conn.close()

def Ajouter_utilisateur():
    while True:
        nom=input('saisir le nom')
        if nom.isnumeric():
            print('nom doit etre une chaine')
        else:
            break
    while True:
        prenom=input('saisir le prenom')
        if prenom.isnumeric():
            print('prenom doit etre une chaine')
        else:
            break
    while True:
        telephone=input('saisir le numero de telephone')
        if (not telephone.isnumeric()  or len(telephone) != 9 or telephone[:2] not in ["77", "78", "70", "71", "76","75"]): 
            print('saisi invalide')
        else:
            break
    while True:
            email=input("saisir l'email")
            if "@" in email and "." in email and " " not in email:
                break
            else:
                print("Le mail saisi n'est pas valide")
    while True:
        print('1: USER')
        print('2: ADMIN')
        choix=input('choisir le role')
        if choix.isnumeric():
            choix=int(choix)
            match choix:
                case 1:
                    role='user'
                    break
                case 2:
                    role='admin'
                    break
                case _:
                    print('Choix invalide')
        else:
            print('vous devez saisir un nombre')
        
    while True:
        mdp=input('saisir le mot de pass')
        if len(mdp)<8:
            print('le mot de pass doit contenir 8 caracteres')
        else:
            # convertir en bytes
            mot_de_passe_bytes = mdp.encode('utf-8')

            # hachage
            hash = bcrypt.hashpw(mot_de_passe_bytes, bcrypt.gensalt())
            break
        
    creer_utilisateur(nom,prenom,telephone,email,hash,role)
def utilisateur_connecter(email,mdp):
    conn=get_connection()
    curseur=conn.cursor()
    try:
        sql='select role,prenom,nom from utilisateurs where email=%s and mot_de_pass=%s'
        curseur.execute(sql,(email,mdp))
        u=curseur.fetchone()
        return u
    except Exception as e:
        print("erreur lors de l'affichage ",e)
    finally:
        curseur.close()
        conn.close()

def afficher_utilisateur():
    conn=get_connection()
    curseur=conn.cursor()
    try:
        sql='select nom,prenom,email,telephone from utilisateurs'
        curseur.execute(sql)
        utilisateurs=curseur.fetchall()
        for u in utilisateurs:
            print(f"Prenom: {u[0]} | Nom: {u[1]} | Email: {u[2]} | Telephone: {u[3]}")
    except Exception as e:
        print("erreur lors de l'affichage ",e)
    finally:
        curseur.close()
        conn.close()

def mot_de_pass_hash(email):
    conn=get_connection()
    curseur=conn.cursor()
    try:
        sql='select mot_de_pass from utilisateurs where email=%s'
        curseur.execute(sql,(email,))
        mdp=curseur.fetchone()
        if mdp==None:
            return mdp
        else:
            return mdp[0]
    except Exception as e:
        print("erreur lors de l'affichage ",e)
    finally:
        curseur.close()
        conn.close()
    
    
    




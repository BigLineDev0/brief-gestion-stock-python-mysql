from db import get_connection
def creer_utilisateur(nom,prenom,telephone,email,mot_de_pass):
    conn=get_connection()
    curseur=conn.cursor()
    try:
        sql='insert into utilisateurs(nom,prenom,telephone,email,mot_de_pass)values(%s,%s,%s,%s,%s)'
        curseur.execute(sql,(nom,prenom,telephone,email,mot_de_pass))
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
        if not telephone.isnumeric() and len(telephone)!=9:
            print('saisi invalide')
        else:
            break
    email=input("saisir l'email")
    while True:
        mdp=input('saisir le mot de pass')
        if len(mdp)<8:
            print('le mot de pass doit contenir 8 caracteres')
        else:
            break
    creer_utilisateur(nom,prenom,telephone,email,mdp)

def afficher_utilisateur(email,mdp):
    conn=get_connection()
    curseur=conn.cursor()
    try:
        sql='select * from utilisateurs where email=%s and mot_de_pass=%s'
        curseur.execute(sql,(email,mdp))
        u=curseur.fetchone()
        return u
    except Exception as e:
        print("erreur lors de l'affichage ",e)
    finally:
        curseur.close()
        conn.close()

def afficherutilisateur():
    conn=get_connection()
    curseur=conn.cursor()
    try:
        sql='select * from utilisateurs'
        curseur.execute(sql)
        utilisateurs=curseur.fetchall()
        return utilisateurs
    except Exception as e:
        print("erreur lors de l'affichage ",e)
    finally:
        curseur.close()
        conn.close()

    
    
    




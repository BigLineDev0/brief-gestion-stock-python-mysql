import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="MotDePasseFort",
            database="gestion_stock"
        )
        return conn
    except Error as e:
        print("Erreur de connexion à la base de données:", e)
        return None
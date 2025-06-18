# Connection à une BD
# Il faut avoir installé mysqlconnector (pip install mysql-connector-python)
# Author : Jaruphong et Gaëtan
# Version 1.0 Date : 10.06.2025


import mysql.connector


def open_db():
    """Établit une connexion à la base de données et retourne l'objet connexion."""
    try:
        conn = mysql.connector.connect(
            host='127.0.0.1',
            port='3306',
            user='root',
            password='Root',
            database="cookingclasses"
        )
        return conn
    except mysql.connector.Error as err:
        print(f"Erreur de connexion : {err}")
        return None


def read_SQL(sql):
    """Exécute une requête SELECT et affiche les résultats."""
    conn = open_db()
    if conn is None:
        return []

    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    except mysql.connector.Error as err:
        print(f"Erreur SQL : {err}")
        return []
    finally:
        cursor.close()
        conn.close()


def read_table(table):
    """Lit le contenu d'une table et retourne une liste de dictionnaires."""
    return read_SQL(f"SELECT * FROM {table}")


def exec_SQL(sql):
    """
    Exécute une requête SQL (INSERT, UPDATE, DELETE, etc.).

    :param sql: Chaîne contenant la requête SQL complète.
    :return: True si la requête s'exécute avec succès, sinon False.
    """
    conn = open_db()
    if conn is None:
        return False

    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        print(f"Requête exécutée avec succès : {sql}")
        return True
    except mysql.connector.Error as err:
        print(f"Erreur lors de l'exécution de la requête : {err}")
        return False
    finally:
        cursor.close()
        conn.close()


def insert_row(table, values):
    """
    Insère un seul enregistrement dans une table.

    :param table: Nom de la table.
    :param values: Dictionnaire représentant une seule ligne à insérer.
                   Ex: {"name": "Cours 1", "datetime": "2025-06-15 20:00:00"}
    """
    if not values:
        print("Aucune donnée à insérer.")
        return False

    conn = open_db()
    if conn is None:
        return False

    try:
        cursor = conn.cursor()

        # Générer les colonnes et les placeholders (%s, %s, ...)
        columns = ", ".join(values.keys())
        placeholders = ", ".join(["%s"] * len(values))

        sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        data = tuple(values.values())
        # print(sql, data)
        cursor.execute(sql, data)
        conn.commit()
        print(f"Enregistrement inséré avec l'ID {cursor.lastrowid}.")
        return True
    except mysql.connector.Error as err:
        print(f"Erreur lors de l'insertion dans {table} : {err}")
        return False
    finally:
        cursor.close()
        conn.close()


def update_row(table, new_values, where):
    """
    Met à jour une ligne dans une table.

    :param table: Nom de la table.
    :param new_values: Dictionnaire des colonnes et nouvelles valeurs {"colonne": valeur}.
    :param where: Dictionnaire des conditions {"colonne": valeur}.
    """
    if not new_values or not where:
        print("Données incomplètes pour la mise à jour.")
        return False

    conn = open_db()
    if conn is None:
        return False

    try:
        cursor = conn.cursor()

        # Construire la requête
        set_clause = ", ".join([f"{key} = %s" for key in new_values.keys()])
        where_clause = " AND ".join([f"{key} = %s" for key in where.keys()])
        sql = f"UPDATE {table} SET {set_clause} WHERE {where_clause}"

        data = tuple(new_values.values()) + tuple(where.values())

        cursor.execute(sql, data)
        conn.commit()
        print(f"{cursor.rowcount} enregistrement(s) mis à jour.")
        return True
    except mysql.connector.Error as err:
        print(f"Erreur lors de la mise à jour dans {table} : {err}")
        return False
    finally:
        cursor.close()
        conn.close()

def delete_row(table, where):
    """
    Supprime un enregistrement d'une table.

    :param table: Nom de la table.
    :param where: Dictionnaire des conditions {"colonne": valeur}.
    """
    if not where:
        print("Une condition WHERE est obligatoire pour la suppression.")
        return False

    conn = open_db()
    if conn is None:
        return False

    try:
        cursor = conn.cursor()

        where_clause = " AND ".join([f"{key} = %s" for key in where.keys()])
        sql = (f"DELETE FROM {table} WHERE {where_clause}")

        cursor.execute(sql, tuple(where.values()))
        conn.commit()
        print(f"{cursor.rowcount} enregistrement(s) supprimé(s).")
        return True
    except mysql.connector.Error as err:
        print(f"Erreur lors de la suppression dans {table} : {err}")
        return False
    finally:
        cursor.close()
        conn.close()

def delete_courses_and_participant(course_id):
    """
    Supprime les inscription liées au cours, puis supprime le cours.

    if not where:
        print("Une condition WHERE est obligatoire pour la suppression.")
        return False
"""
    conn = open_db()
    if conn is None:
        return False

    try:
        cursor = conn.cursor()

        # Supprimer les inscriptions liées
        sql_participants = "DELETE FROM participants_has_cook_courses WHERE id = %s"
        cursor.execute(sql_participants, (course_id,))

        # Supprimer le cours
        sql_course = "DELETE FROM cook_courses WHERE id = %s"
        cursor.execute(sql_course, (course_id,))

        conn.commit()

        print(f"{cursor.rowcount} enregistrement(s) supprimé(s).")
        return True

    except mysql.connector.Error as err:
        print(f"Erreur lors de la suppression : {err}")
        return False

    finally:
        cursor.close()
        conn.close()

# Exemples d'utilisation
if __name__ == "__main__":

    # Test de read_SQL
    data = read_table("participants_has_cook_courses")
    # print(data)  # affichage complet
    # for row in data:  # affichage ligne par ligne
    #     print(row)

def get_participants_courses():
    """
    Retourne la liste des inscriptions avec noms complets des participants et noms de cours.
    Les triples guillemet servent à définir des chaîne de caractères multi-lignes et plus lisible (aide de chatGPT)
    """
    sql = """
        SELECT 
            participants_has_cook_courses.id,
            participants.first_name,
            participants.last_name,
            cook_courses.name AS course_name
        FROM 
            participants_has_cook_courses
        JOIN 
            participants ON participants_has_cook_courses.participants_id = participants.id
        JOIN 
            cook_courses ON participants_has_cook_courses.cook_courses_id = cook_courses.id
        ORDER BY 
            cook_courses.id ASC
    """
    return read_SQL(sql)

def get_course(course_id):
    # récupérer les informations d'un cours à partir de ID
    results = read_SQL(f"SELECT * FROM cook_courses WHERE id = {course_id}")
    return results[0] if results else None # Un dictionnaire retourne le premier résultat sinon rien

# compter le nombre de participants
def count_inscriptions(course_id):
    results = read_SQL(f"SELECT COUNT(*) AS total FROM participants_has_cook_courses WHERE cook_courses_id = {course_id}")
    return results[0]["total"] if results else 0

def contenu_deroulant_participants():
    sql = "SELECT first_name, last_name FROM participants"
    return read_SQL(sql)

def contenu_deroulant_cours():
    sql = "SELECT name FROM cook_courses"
    return read_SQL(sql)

def traduction_participants(participants):

    # aide de ChatGPT pour pouvoir ajouter une personne avec plusieurs prénoms et noms
    parts = participants.strip().split()

    if len(parts) < 2:
        print("Format de nom invalide (il faut au moins un prénom et un nom)")
        return None

    for i in range(1, len(parts)):
        first_name = " ".join(parts[:i])
        last_name = " ".join(parts[i:])
        # Insérer et introduire le prénom et nom dans la base SQL avec '{ }'
        sql = f"SELECT id FROM participants WHERE first_name = '{first_name}' AND last_name = '{last_name}'"
        try:
            result = read_SQL(sql)
            if result:
                row = result[0]
                return row["id"] if isinstance(row, dict) else row[0]
        except mysql.connector.Error as err:
            print(f"Erreur lors de la suppression : {err}")
            return None

def traduction_course(course):
    sql = f"""
            SELECT 
                id
            FROM 
                cook_courses
            WHERE 
                name = '{course}'
                """ # Cette manière n'est pas très sécurisée, mais elle a au moins le mérite de fonctionner
    result = read_SQL(sql)

    if result:
        row = result[0]
        if isinstance(row, dict):
            return row['id']
        elif isinstance(row, tuple):
            return row[0]


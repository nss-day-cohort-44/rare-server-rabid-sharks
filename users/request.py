import sqlite3
import json

from models import USER

def get_all_users():
    # Open a connection to the database
    with sqlite3.connect("./rare.db") as conn:
        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            u.id,
            u.first_name,
            u.last_name,
            u.email,
            u.bio,
            u.username,
            u.profile_image_url,
            u.created_on,
            u.active,
            account_type_id
        FROM User u
        """)

        users = []

        dataset= db_cursor.fetchall()

        for row in dataset:

            user = USER(row["id"],row["first_name"],row["last_name"],row["email"],row["bio"],row["username"],row["profile_image_url"],row["created_on"],row["active"],row["account_type_id"])

            users.append(user.__dict__)
        
    return json.dumps(users)

def get_single_users(id):
    # Open a connection to the database
    with sqlite3.connect("./rare.db") as conn:
        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            u.id,
            u.first_name,
            u.last_name,
            u.email,
            u.bio,
            u.username,
            u.profile_image_url,
            u.created_on,
            u.active,
            account_type_id
        FROM User u
        """, (id,))

        data= db_cursor.fetchone()


        user = USER(data["id"],data["first_name"],data["last_name"],data["email"],data["bio"],data["username"],data["profile_image_url"],data["created_on"],data["active"],data["account_type_id"])

            users.append(user.__dict__)
        
    return json.dumps(users)    
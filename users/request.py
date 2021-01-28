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
            u.password,
            u.bio,
            u.username,
            u.profile_image_url,
            u.created_on,
            u.active,
            u.account_type_id
        FROM Users u
        """)

        users = []

        dataset= db_cursor.fetchall()

        for row in dataset:

            user = USER(row["id"], row["first_name"], row["last_name"], row["email"], row["password"], row["bio"], row["username"], row["profile_image_url"], row["created_on"], row["active"], row["account_type_id"])

            users.append(user.__dict__)
        
    return json.dumps(users)

def get_single_user(id):
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
            u.password,
            u.bio,
            u.username,
            u.profile_image_url,
            u.created_on,
            u.active,
            u.account_type_id
        FROM Users u
        WHERE id = ?
        """, (id, ))

        data= db_cursor.fetchone()


        user = USER(data["id"],data["first_name"],data["last_name"],data["email"],data["password"],data["bio"],data["username"],data["profile_image_url"],data["created_on"],data["active"],data["account_type_id"])

    return json.dumps(user.__dict__)    

def get_user_by_email(email):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            u.id,
            u.first_name,
            u.last_name,
            u.email,
            u.password,
            u.bio,
            u.username,
            u.profile_image_url,
            u.created_on,
            u.active,
            u.account_type_id
        FROM Users u
        WHERE u.email = ?
        """, (email, ))


        data= db_cursor.fetchone()

        user = USER(data["id"],data["first_name"],data["last_name"],data["email"],data["password"],data["bio"],data["username"],data["profile_image_url"],data["created_on"],data["active"],data["account_type_id"])

    return json.dumps(user)


def create_user(new_user):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO USERS
            ( first_name, last_name, email, password, bio, username, created_on, profile_image_url, active, account_type_id )
        VALUES
            ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """, (new_user['first_name'], new_user['last_name'],
              new_user['email'], new_user['password'] , new_user['bio'],
              new_user['username'], new_user["created_on"], new_user['profile_image_url'],new_user['active'],new_user['account_type_id']))

        id = db_cursor.lastrowid

    return json.dumps(new_user)

def update_user(id, new_user):
    # Open a connection to the database
    with sqlite3.connect("./rare.db") as conn:
        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Users
            SET
                first_name = ?,
                last_name = ?,
                email = ?,
                password = ?,
                bio = ?,
                username = ?,
                profile_image_url = ?,
                created_on = ?,
                active = ?,
                account_type_id = ?
        WHERE id = ?
        """, (new_user["first_name"], new_user["last_name"], new_user["email"], new_user["password"], new_user["bio"], new_user["username"], new_user["profile_image_url"], new_user["created_on"], new_user["active"], new_user["account_type_id"], id, ))

        rows_affected = db_cursor.rowcount
    if rows_affected == 0:
        return False
    else:
        return True



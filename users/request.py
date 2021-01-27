import sqlite3
import json

def get_allusers():
    # Open a connection to the database
    with sqlite3.connect("./kennel.db") as conn:
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
import sqlite3
import json
from models import Tag


def get_all_tags():
    # Open a connection to the database
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            t.id,
            t.label
        FROM Tag t
        """)

        # Initialize an empty list to hold all tag representations
        tags = []
        dataset = db_cursor.fetchall()

        # Iterate all rows of data returned from database
        for row in dataset:

            # Create an tag instance from the current row
            tag = Tag(row['id'], row['label'])


            tags.append(tag.__dict__)

    return json.dumps(tags)


def get_single_tag(id):
    # Open a connection to the database
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            t.id,
            t.label
        FROM Tag t
        """, (id, ))

        data = db_cursor.fetchone()

        # Create an tag instance from the current row
        tag = Tag(data['id'], data['label'])

        return json.dumps(tag.__dict__)


def create_tag(new_tag):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Tag
            ( label )
        VALUES
            ( ? );
        """, ( new_tag['label'] )
        )

        id = db_cursor.lastrowid
        new_tag['id'] = id


    return json.dumps(new_tag)


def update_tag(id, new_tag):
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Tag
            SET
                label = ?
        WHERE id = ?
        """, (
                new_tag['label'],
                id,
             )
        )

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True


def delete_tag(id):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM tag
        WHERE id = ?
        """, (id, ))

        rows_affected = db_cursor.rowcount  # 0 or 1

        if rows_affected == 0:
            return False
        else:
            return True
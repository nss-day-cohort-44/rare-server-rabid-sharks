import sqlite3
import json
from models import Comment

def get_all_comments():
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        # write the SQL QUERY
        db_cursor.execute("""
        SELECT
            c.id,
            c.post_id,
            c.author_id,
            c.content,
            c.created_on
        FROM Comments c
        """)
        # inittialize new empty LIST to hold all the emp DICTs
        comments = []
        # convert rows of data into a PYTHON LIST
        dataset = db_cursor.fetchall()
        # iterate the list
        for row in dataset:
            comment = Comment(row['id'], row['post_id'], 
                                row['author_id'], row['content'], row['created_on'],)
            comments.append(comment.__dict__)
    return json.dumps(comments)

def get_single_comment(id):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
        SELECT
            c.id,
            c.post_id,
            c.author_id,
            c.content,
            c.created_on
        FROM Comments c
        WHERE c.id = ?
        """, (id,))
        data = db_cursor.fetchone()
        comment = Comment(data['id'], data['post_id'],
                            data['author_id'], data['content'],
                            data['created_on'])
        return json.dumps(comment.__dict__)

def get_comments_by_post_id(post_id):
    with sqlite3.connect('./rare.db') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        # Write teh SQL query to get the information you want
        db_cursor.execute("""
        SELECT  
            c.id,
            c.post_id,
            c.author_id,
            c.content,
            c.created_on
        FROM Comments c
        WHERE c.post_id = ?
        """, ( post_id, ))

        comments = []
        dataset = db_cursor.fetchall()
        for row in dataset:
            comment = Comment(row['id'], row['post_id'],
                                row['author_id'], row['content'], 
                                row['created_on'])
            comments.append(comment.__dict__)

    return json.dumps(comments)

def delete_comment(id):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute(""" 
        DELETE FROM Comments
        WHERE id = ?
        """, (id, ))

def update_comment(id, new_comment):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()
        db_cursor.execute(""" 
        UPDATE Comments
            Set
                post_id = ?,
                author_id = ?,
                content = ?,
                created_on = ?
        WHERE id = ?
        """, (new_comment['post_id'], new_comment['author_id'], 
                new_comment['content'], new_comment['created_on'], id, ))
        # count the rows affected and check if the id provided exists
        rows_affected = db_cursor.rowcount
    if rows_affected == 0:
        # forces 404 response by the main module
        return False
    else:
        # forces 204 response
        return True

def create_comment(new_comment):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Comments
            ( post_id, author_id, content, created_on )
        VALUES
            ( ?, ?, ?, ? );
        """, (new_comment['post_id'], new_comment['author_id'], 
            new_comment['content'], new_comment['created_on'], ))
# The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid
        # Add the 'id' property to the comment dict that
        # waws sent by client so client can see the primary key in the repsonse.
        new_comment['id'] = id
    return json.dumps(new_comment)
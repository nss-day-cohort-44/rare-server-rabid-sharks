from models import Post_tag
from models import Tag
import sqlite3
import json

def get_all_Post_tags():
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            pt.id,
            pt.post_id,
            pt.tag_id,
            t.label
        FROM PostTags pt
        JOIN Tags t
            ON pt.tag_id = t.id
        """)

        post_tags = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            post_tag = Post_tag(row['id'], row['post_id'], row['tag_id'])

            tag = Tag(row['id'], row['label'])

            post_tag.tag = tag.__dict__
            
            post_tags.append(post_tag.__dict__)
    return json.dumps(post_tags)

def create_post_tag(new_post_tag):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO PostTags
            (post_id, tag_id)
        VALUES
            (?,?);
        """, (new_post_tag['post_id'], new_post_tag['tag_id'], ))

        id = db_cursor.lastrowid

        new_post_tag['id'] = id

    return json.dumps(new_post_tag)


def update_post_tag(id, new_post_tag):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE PostTags
            SET
                post_id = ?,
                tag_id = ?
        WHERE id = ?
        """, (new_post_tag['post_id'], new_post_tag['tag_id'], id, ))

        rows_affected = db_cursor.rowcount

        if rows_affected == 0:
            return False
        else:
            return True

def get_post_tags_by_post_id(post_id):
    with sqlite3.connect("./rare.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            pt.id,
            pt.post_id,
            pt.tag_id,
            t.label
        FROM PostTags pt
        JOIN Tags t
            ON pt.tag_id = t.id
        WHERE pt.post_id = ?
        """, (post_id, ))

        post_tags = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            post_tag = Post_tag(row['id'], row['post_id'], row['tag_id'])

            tag = Tag(row['id'], row['label'])

            post_tag.tag = tag.__dict__
            
            post_tags.append(post_tag.__dict__)
    return json.dumps(post_tags)

def delete_post_tag(id):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM PostTags
        WHERE id = ?
        """, (id, ))

def accept_tag_array_by_post_id(tag_dict):
    with sqlite3.connect("./rare.db") as conn:
        db_cursor = conn.cursor()
        for (tags) in tag_dict['tag_array']:
            db_cursor.execute("""
            INSERT INTO PostTags
                (post_id, tag_id)
            VALUES
                (?,?);
            """, (tag_dict['post_id'], tags, ))
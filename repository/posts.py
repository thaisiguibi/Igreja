from core.db import get_connection

def create_post(title, content, user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO posts (title, content, user_id, active)
    VALUES (?, ?, ?, 1)
                   """, (title, content, user_id))

    conn.commit()
    post_id = cursor.lastrowid
    conn.close()

    return post_id

def get_posts(limit, offset, title=None, order="asc"):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT
    p.id,
    p.title,
    p.content,
    u.id as user_id,
    u.name
    FROM posts p
    JOIN users u ON p.user_id = u.id
    WHERE p.active = 1
    """

    params = []

    if title:
        query += " AND p.title LIKE ? "
        params.append(f"%{title}%")

    if order.lower() == "desc":
        query += " ORDER BY p.id DESC "
    else:
        query += " ORDER BY p.id ASC "

    query += " LIMIT ? OFFSET ? "
    params.extend([limit, offset])

    cursor.execute(query, params)
    rows = cursor.fetchall()

    total = count_posts(title)

    conn.close()

    return [
    {
        "id": r["id"],
        "title": r["title"],
        "content": r["content"],
        "user": {
            "id": r["user_id"],
            "name": r["name"]
        }
    }
    for r in rows
], total


def delete_post(post_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
            "UPDATE posts SET active = 0 WHERE id = ?",
            (post_id,)
            )
    conn.commit()
    conn.close()
    
    return True

def get_post(post_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        p.id,
        p.title,
        p.content,
        u.id as user_id,
        u.name
    FROM posts p
    JOIN users u ON p.user_id = u.id
    WHERE p.id = ? AND p.active = 1
    """, (post_id,))

    row = cursor.fetchone()
    conn.close()

    if not row:
        return None

    return {
        "id": row["id"],
        "title": row["title"],
        "content": row["content"],
        "user": {
            "id": row["user_id"],
            "name": row["name"]
        }
    }


def update_post(post_id, title, content):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
    """
    UPDATE posts
    SET title = ?, 
    content = ?
    WHERE id = ? AND active = 1
    """, (title, content, post_id))

    conn.commit()
    conn.close()


def get_post_raw(post_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT id, title, content, user_id
    FROM posts
    WHERE id = ? AND active = 1
                   """, (post_id,)
                   )

    row = cursor.fetchone()
    conn.close()

    return dict(row) if row else None

def count_posts(title=None):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT COUNT(*)
    FROM posts
    WHERE active = 1
    """

    params = []

    if title:
        query += " AND title LIKE ?"
        params.append(f"%{title}%")

    cursor.execute(query, params)
    total = cursor.fetchone()[0]

    conn.close()
    
    return total

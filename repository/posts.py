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
    u.id,
    u.name
    FROM posts p
    JOIN users u ON p.user_id = u.id
    WHERE p.active = 1
    """
    params = []

#filtro
    if title: 
        query += " AND p.title LIKE ? "
        params.append(f"%{title}%")

#ordenação
    if order.lower() == "desc":
        query += " ORDER BY p.id DESC "
    else:
        query += "ORDER BY p.id ASC "

#paginação
    query += " LIMIT ? OFFSET? "
    params.extend([limit, offset])

    cursor.execute(query, params)
 
    rows = cursor.fetchall()
    conn.close()

    return rows
    

def create_post(title, content, user_id):
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute(
            """
            INSERT INTO posts (title, content, user_id, active)
            VALUES (?, ?, ?, 1)
            """,
            (title, content, user_id)
            )
    conn.commit()
    post_id = cursor.lastrowid
    conn.close()
 
    return post_id

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

def get_post_by_id(post_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
            "SELECT * FROM posts WHERE id = ? AND active = 1",
            (post_id,)
            )
    row = cursor.fetchone()
    conn.close()

    return dict(row) if row else None


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

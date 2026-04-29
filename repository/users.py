from core.db import get_connection

def get_users(limit, offset):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT id, name, active
    FROM users
    WHERE active = 1
    LIMIT ? OFFSET ?
                   """, (limit, offset))

    rows = cursor.fetchall()


    cursor.execute("""
    SELECT COUNT(*)
    FROM users
    WHERE active = 1
                   """)
    total = cursor.fetchone()[0]

    conn.close()

    return [dict(r) for r in rows], total


def create_user(name, password):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
            INSERT INTO users (name, password)
            VALUES (?, ?)
                   """,
            (name, password)
            )

    conn.commit()
    user_id = cursor.lastrowid                                                
    conn.close()
    return user_id

def deactivate_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
            "UPDATE users SET active = 0 WHERE id = ?",
            (user_id,)
            )
    conn.commit()
    conn.close()

def get_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
            "SELECT * FROM users WHERE id = ?",
            (user_id,)
            )
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None

def get_user_by_name(name):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
                   SELECT id, name, password 
                   FROM users 
                   WHERE name = ?
                   """,
                   (name,)
                   )

    row = cursor.fetchone()
    conn.close()

    if not row:
        return None

    return {
            "id": row[0],
            "name": row[1],
            "password": row[2]
            }

def count_users():
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
    SELECT COUNT(*) 
    FROM users 
    WHERE active = 1
                   """
                   )
    total = cursor.fetchone()[0]

    conn.close()
    return total

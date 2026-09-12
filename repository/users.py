from core.db import get_connection, execute, DATABASE_URL


def get_users(limit, offset):
    conn = get_connection()
    cursor = conn.cursor()

    execute(cursor, """
        SELECT id, name, active
        FROM users
        WHERE active = 1
        LIMIT ? OFFSET ?
    """, (limit, offset))

    rows = cursor.fetchall()

    execute(cursor, """
        SELECT COUNT(*) AS total
        FROM users
        WHERE active = 1
    """)

    total = cursor.fetchone()["total"]

    conn.close()

    return [dict(r) for r in rows], total


def create_user(name, password):
    conn = get_connection()
    cursor = conn.cursor()

    if DATABASE_URL:
        execute(cursor, """
            INSERT INTO users (name, password, active)
            VALUES (?, ?, 1)
            RETURNING id
        """, (name, password))

        user_id = cursor.fetchone()["id"]

    else:
        execute(cursor, """
            INSERT INTO users (name, password, active)
            VALUES (?, ?, 1)
        """, (name, password))

        user_id = cursor.lastrowid

    conn.commit()
    conn.close()

    return user_id


def deactivate_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    execute(cursor, """
        UPDATE users
        SET active = 0
        WHERE id = ?
    """, (user_id,))

    conn.commit()
    conn.close()

    return True


def get_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    execute(cursor, """
        SELECT id, name, active
        FROM users
        WHERE id = ?
        AND active = 1
    """, (user_id,))

    row = cursor.fetchone()

    conn.close()

    return dict(row) if row else None


def get_user_by_name(name):
    conn = get_connection()
    cursor = conn.cursor()

    execute(cursor, """
        SELECT id, name, password, active
        FROM users
        WHERE name = ?
    """, (name,))

    row = cursor.fetchone()

    conn.close()

    if not row:
        return None

    return {
        "id": row["id"],
        "name": row["name"],
        "password": row["password"],
        "active": row["active"]
    }


def count_users():
    conn = get_connection()
    cursor = conn.cursor()

    execute(cursor, """
        SELECT COUNT(*) AS total
        FROM users
        WHERE active = 1
    """)

    total = cursor.fetchone()["total"]

    conn.close()

    return total

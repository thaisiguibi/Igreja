from core.db import get_connection

def create_subscription(email):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO newsletter (email, active)
    VALUES (?, 1)
                   """, 
                   (email,)
                   )
    conn.commit()
    conn.close()

    return True


def get_subscribers():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT id, email
    FROM newsletter
    WHERE active = 1
                   """
                   )

    rows = cursor.fetchall()
    conn.close()

    return [dict(r) for r in rows]

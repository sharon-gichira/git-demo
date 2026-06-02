from db_config import get_connection


sql = '''
    insert into students(name, city, score)
    VALUES(%s,%s,%s)
    RETURNING id
'''

with get_connection() as conn:
    with conn.cursor() as cur:
        cur.execute(sql, ('Joyce', 'Nairobi', 89))
        new_id = cur.fetchone()[0]        
        conn.commit()
        print(f"Inserted students ID = {new_id}")
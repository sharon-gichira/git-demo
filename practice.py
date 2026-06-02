from db_config import get_connection

with get_connection() as conn:
    with conn.cursor() as cur:
        cur.execute('''
                CREATE TABLE IF NOT EXISTS students(
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    city varchar(80),
                    score NUMERIC(5,2))
                    ''')
    print('Table Ready')
        
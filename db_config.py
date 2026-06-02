import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

DB = {
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'port': os.getenv('DB_PORT')
}

if not all(DB.values()):
    raise ValueError('Missing DB credentials check your .env file')

def get_connection():
    return psycopg2.connect(**DB)
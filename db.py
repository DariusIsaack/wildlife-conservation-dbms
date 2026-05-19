import psycopg2
import os

def get_connection():

    database_url = os.getenv("DATABASE_URL")

    conn = psycopg2.connect(database_url)

    return conn
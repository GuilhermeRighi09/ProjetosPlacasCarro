import psycopg2

def get_connection():
    conn = psycopg2.connect(
        host='localhost',
        database='placa_projeto',
        user='postgres',
        password='1234'
    )
    return conn
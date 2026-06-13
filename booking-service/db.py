import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="appointment_db",
    user="postgres",
    password="postgres"
)

cursor = conn.cursor()
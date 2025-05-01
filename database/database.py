import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Read from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# Establish connection
conn = psycopg2.connect(
    host=DB_HOST,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)

cur = conn.cursor()

# Create table if not exists
cur.execute("""
CREATE TABLE IF NOT EXISTS posts (
    id SERIAL PRIMARY KEY,
    text TEXT,
    sentiment VARCHAR(20),
    score FLOAT
)
""")
conn.commit()

def insert_post(text, sentiment, score):
    cur.execute("INSERT INTO posts (text, sentiment, score) VALUES (%s, %s, %s)", (text, sentiment, score))
    conn.commit()

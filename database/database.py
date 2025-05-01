## <---------- Import necessary libraries ---------->
import psycopg2  ## PostgreSQL database adapter for Python
import os        ## For interacting with the operating system
from dotenv import load_dotenv  ## For loading environment variables from a .env file

## <---------- Load environment variables from .env file ---------->
load_dotenv()  ## Reads the .env file and loads environment variables

## <---------- Read database configuration from environment variables ---------->
DB_HOST = os.getenv("DB_HOST")        ## Host address of the PostgreSQL server
DB_NAME = os.getenv("DB_NAME")        ## Database name
DB_USER = os.getenv("DB_USER")        ## Database username
DB_PASSWORD = os.getenv("DB_PASSWORD")## Database password

## <---------- Establish connection to PostgreSQL database ---------->
conn = psycopg2.connect(              ## Connect to the PostgreSQL database using credentials
    host=DB_HOST,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)

cur = conn.cursor()  ## Create a cursor object to interact with the database

## <---------- Create posts table if it doesn't exist ---------->
cur.execute("""                          ## SQL command to create table if it doesn't exist
CREATE TABLE IF NOT EXISTS posts (
    id SERIAL PRIMARY KEY,              ## Auto-incrementing ID as the primary key
    text TEXT,                          ## Column for the text content
    sentiment VARCHAR(20),             ## Column for the sentiment label (e.g., Positive, Negative)
    score FLOAT                         ## Column for the sentiment score
)
""")
conn.commit()  ## Commit the transaction to make changes persistent

## <---------- Function to insert a post record into the posts table ---------->
def insert_post(text, sentiment, score):  ## Inserts a post with sentiment analysis result
    cur.execute("INSERT INTO posts (text, sentiment, score) VALUES (%s, %s, %s)", (text, sentiment, score))
    conn.commit()  ## Commit after insertion to save the changes

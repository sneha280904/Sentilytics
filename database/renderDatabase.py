## <---------- Import necessary libraries ---------->
import psycopg2                    ## PostgreSQL database adapter for Python
import os                          ## For interacting with the operating system
from dotenv import load_dotenv     ## For loading environment variables from a .env file

## <---------- Load environment variables from .env file ---------->
load_dotenv()       ## Reads the .env file and loads environment variables

## <---------- Read database configuration from environment variables ---------->
DB_HOST = os.getenv("DB_HOST")            ## Host address of the PostgreSQL server
DB_NAME = os.getenv("DB_NAME")            ## Database name
DB_USER = os.getenv("DB_USER")            ## Database username
DB_PASSWORD = os.getenv("DB_PASSWORD")    ## Database password


import os

DATABASE_URL = os.getenv("DATABASE_URL")

conn = psycopg2.connect(DATABASE_URL)  ## Read from env variable


cur = conn.cursor()        ## Create a cursor object to interact with the database

## <---------- Create posts table if it doesn't exist ---------->
cur.execute("""                          
CREATE TABLE IF NOT EXISTS posts (
    id SERIAL PRIMARY KEY,
    text TEXT,
    model TEXT,
    sentiment VARCHAR(20),
    score FLOAT 
)
""")
conn.commit()               ## Commit the transaction to make changes persistent

## <---------- Function to insert a post record into the posts table with exception handling ---------->

def insert_post(text, model, sentiment, score):              ## Function to insert a post into the posts table
    try:                                                      ## Try block to attempt the insertion
        cur.execute(                                          ## Execute the SQL insert query using psycopg2
            "INSERT INTO posts (text, model, sentiment, score) VALUES (%s, %s, %s, %s)",  ## SQL insert statement with 4 placeholders
            (text, model, sentiment, score)                  ## Values to be inserted into the table
        )
        conn.commit()                                         ## Commit the transaction if insertion is successful
    except Exception as e:                                    ## If any error occurs during the transaction
        conn.rollback()                                       ## Rollback the transaction to clear failed state
        print("Error inserting post:", e)                     ## Print the error message for debugging

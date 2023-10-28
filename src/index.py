from database import connection
from dotenv import load_dotenv
import os

load_dotenv()

conn = connection.Database(os.getenv("DB_URI"), os.getenv("DB_NAME"), os.getenv("DB_COLL"))

try:
    conn
    print("Connected!")
except Exception as e:
    print(f"Error: {e}")

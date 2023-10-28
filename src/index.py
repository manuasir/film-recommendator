from database import connection
from api import api
from dotenv import load_dotenv
import os

load_dotenv()

# Conexión con MongoDB
conn = connection.Database(os.getenv("DB_URI"), os.getenv("DB_NAME"), os.getenv("DB_COLL"))

# Llamada a la API
api_instance = api.API(conn, os.getenv("API_KEY"), "https://api.themoviedb.org/3", 1, 5)

try:
  api_instance.store_films()
except Exception as e:
  print(f"Error: {e}")
